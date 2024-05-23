"""
SiteSelector.py -- Select observing position

Requirements
============

naojsoft packages
-----------------
- ginga
"""
# stdlib
import os.path
from datetime import datetime
from dateutil import tz, parser

# ginga
from ginga.gw import Widgets, GwHelp
from ginga import GingaPlugin
from ginga.misc.Callback import Callbacks
from ginga.util.paths import ginga_home

# 3rd party
import yaml

# local
from spot.util import sites

# where our config files are stored
from spot import __file__
cfgdir = os.path.join(os.path.dirname(__file__), 'config')


class SiteSelector(GingaPlugin.LocalPlugin):
    """
    SiteSelector
    ============
    The SiteSelector plugin is used to select the location from where you
    are planning to observe, as well as the time of observation at that
    location.

    You will almost always want to start this plugin first, because it
    controls many of the aspects of the other plugins visible on the workspace.

    Setting the observing location
    ------------------------------
    Use the "Site:" drop-down menu to select the observing location.  There
    are a number of predefined sites available.

    Adding your own custom observing location
    -----------------------------------------
    If your desired location is not available, you can easily add your own.
    If you have the SPOT source code checked out, you can find the file
    "sites.yml" in .../spot/spot/config/.  Copy this file to $HOME/.spot
    and edit it to add your own site.  Be sure to set all of the keywords
    for your site (latitude, longitude, elevation, etc).  Restart spot and
    you should be able to see your new location.

    Setting the time of observation
    -------------------------------
    The time can be set to the current time or a fixed time. To set to the
    current time, chose "Now" from the "Time mode:" drop-down menu.

    To set a fixed time, chose "Fixed"--this will enable the "Date time:"
    and "UTC offset (min):" controls.  Enter the date/time in the first box
    in the format YYYY-MM-DD HH:MM:SS and press "Set".

    By default the UTC offset of the fixed time will be set to that of the
    timezone of the observing location; but you can enter a custom offset
    (in *minutes*) from UTC in the other box and press "Set" to indicate
    a special offset for interpreting the time.

    .. note:: this does NOT change the timezone of the observing location;
              it just sets the interpretation of the fixed time you are
              setting.

    Updating of plugins
    -------------------
    Whenever you change the observing location or the time, the other plugins
    should update automatically (if they subscribe for site and time changes,
    which most are designed to do).
    """
    def __init__(self, fv, fitsimage):
        super().__init__(fv, fitsimage)

        # get SiteSelector preferences
        prefs = self.fv.get_preferences()
        self.settings = prefs.create_category('plugin_SiteSelector')
        self.settings.add_defaults(default_site=None,
                                   timer_update_interval=1.0)
        self.settings.load(onError='silent')

        self.cb = Callbacks()
        for name in ['site-changed', 'time-changed']:
            self.cb.enable_callback(name)

        # see if user has a custom list of sites
        path = os.path.join(ginga_home, "sites.yml")
        if not os.path.exists(path):
            # open stock list of sites
            path = os.path.join(cfgdir, "sites.yml")

        # configure sites
        with open(path, 'r') as site_f:
            sites.configure_sites(yaml.safe_load(site_f))

        self.site_dict = dict()
        site_names = sites.get_site_names()
        for site_name in site_names:
            site = sites.get_site(site_name)
            # mapping from full name to short name
            self.site_dict[str(site)] = site_name

        default_site = self.settings.get('default_site', None)
        if default_site is None:
            default_site = site_names[0]
        self.site_obj = sites.get_site(default_site)
        self.site_obj.initialize()
        self.status = self.site_obj.get_status()

        self.time_mode = 'now'
        self.cur_tz = tz.tzoffset(self.status.timezone_name,
                                  self.status.timezone_offset_min * 60)
        self.dt_utc = datetime.now(tz=tz.UTC)

        self.tmr = GwHelp.Timer(duration=self.settings['timer_update_interval'])
        self.tmr.add_callback('expired', self.update_timer_cb)

        self.gui_up = False

    def build_gui(self, container):

        top = Widgets.VBox()
        top.set_border_width(4)

        fr = Widgets.Frame("Observing Location")
        captions = (("Site:", 'label', 'site', 'combobox'),
                    )
        w, b = Widgets.build_info(captions)
        self.w = b
        fr.set_widget(w)
        top.add_widget(fr, stretch=0)

        for full_name, site_name in self.site_dict.items():
            b.site.insert_alpha(full_name)
        b.site.set_text(str(self.site_obj))
        b.site.add_callback('activated', self.site_changed_cb)

        fr = Widgets.Frame("Time")

        vbox = Widgets.VBox()
        captions = (("Time mode:", 'llabel', "mode", 'combobox'),
                    )

        w, b = Widgets.build_info(captions)
        self.w.update(b)

        for name in 'Now', 'Fixed':
            b.mode.append_text(name)
        b.mode.set_index(0)
        b.mode.set_tooltip("Now or fixed time for visibility calculations")
        b.mode.add_callback('activated', self.set_datetime_cb)
        vbox.add_widget(w, stretch=0)

        captions = (("Date time:", 'llabel', 'datetime', 'entryset'),
                    ("UTC offset (min):", 'llabel', 'timeoff', 'entryset'),
                    )

        w, b = Widgets.build_info(captions)
        self.w.update(b)
        b.datetime.set_tooltip("Set date time for visibility calculations")
        b.datetime.add_callback('activated', self.set_datetime_cb)
        b.datetime.set_enabled(False)
        b.timeoff.set_text(str(self.status.timezone_offset_min))
        b.timeoff.set_tooltip("UTC offset for setting fixed time")
        b.timeoff.set_enabled(False)
        b.timeoff.add_callback('activated', self.set_timeoff_cb)
        self.set_datetime_cb()
        vbox.add_widget(w, stretch=0)

        fr.set_widget(vbox)
        top.add_widget(fr, stretch=0)

        top.add_widget(Widgets.Label(''), stretch=1)

        btns = Widgets.HBox()
        btns.set_border_width(4)
        btns.set_spacing(3)

        btn = Widgets.Button("Close")
        btn.add_callback('activated', lambda w: self.close())
        btns.add_widget(btn, stretch=0)
        btn = Widgets.Button("Help")
        btn.add_callback('activated', lambda w: self.help())
        btns.add_widget(btn, stretch=0)
        btns.add_widget(Widgets.Label(''), stretch=1)

        top.add_widget(btns, stretch=0)

        container.add_widget(top, stretch=1)
        self.gui_up = True

    def close(self):
        self.fv.stop_local_plugin(self.chname, str(self))
        return True

    def help(self):
        name = str(self).capitalize()
        self.fv.help_text(name, self.__doc__, trim_pfx=4)

    def start(self):
        self.update_timer_cb(self.tmr)

    def stop(self):
        self.gui_up = False

    def get_site(self):
        return self.site_obj

    def get_status(self):
        return self.status

    def get_datetime(self):
        return (self.dt_utc, self.cur_tz)

    def site_changed_cb(self, w, idx):
        full_name = w.get_text()
        site_name = self.site_dict[full_name]
        self.site_obj = sites.get_site(site_name)
        self.site_obj.initialize()
        self.status = self.site_obj.get_status()

        # change time zone to be that of the site
        zone_off_min = self.status.timezone_offset_min
        self.w.timeoff.set_text(str(zone_off_min))
        self.cur_tz = tz.tzoffset(self.status.timezone_name,
                                  zone_off_min * 60)
        self._set_datetime()
        self.cb.make_callback('site-changed', self.site_obj)

    def update_timer_cb(self, timer):
        timer.start()

        # get any updated status from the site
        self.status.update(self.site_obj.fetch_status())

        if self.time_mode == 'now':
            self.dt_utc = datetime.now(tz=tz.UTC)
            dt = self.dt_utc.astimezone(self.cur_tz)
            if self.gui_up:
                self.w.datetime.set_text(dt.strftime("%Y-%m-%d %H:%M:%S"))

            self.cb.make_callback('time-changed', self.dt_utc, self.cur_tz)

    def set_timeoff_cb(self, w):
        zone_off_min = int(w.get_text().strip())
        self.cur_tz = tz.tzoffset('Custom', zone_off_min * 60)

        self._set_datetime()

    def set_datetime_cb(self, *args):
        self.time_mode = self.w.mode.get_text().lower()
        self._set_datetime()

    def _set_datetime(self):
        if self.time_mode == 'now':
            self.dt_utc = datetime.now(tz=tz.UTC)
            dt = self.dt_utc.astimezone(self.cur_tz)
            self.w.datetime.set_text(dt.strftime("%Y-%m-%d %H:%M:%S"))
            self.w.datetime.set_enabled(False)
            self.w.timeoff.set_enabled(False)
        else:
            self.w.datetime.set_enabled(True)
            self.w.timeoff.set_enabled(True)
            dt_str = self.w.datetime.get_text().strip()
            dt = parser.parse(dt_str).replace(tzinfo=self.cur_tz)
            self.dt_utc = dt.astimezone(tz.UTC)

        #self.site_obj.observer.set_date(self.dt_utc)

        self.logger.info("date/time set to: {}".format(self.dt_utc.strftime("%Y-%m-%d %H:%M:%S %z")))
        self.cb.make_callback('time-changed', self.dt_utc, self.cur_tz)

    def __str__(self):
        return 'siteselector'
