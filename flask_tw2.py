import tw2.core as twc

class TW2(object):
    def __init__(self, app):
        self.app = app
        self.app.extensions['toscawidgets'] = self
        config = self.extract_config(self.app)
        self.mw = twc.make_middleware(self.app.wsgi_app, **config)
        self.app.wsgi_app = self.mw
    
    def extract_config(self, app):
        config = {}
        g = app.config.get
        config["translator"] = g("TW2_TRANSLATOR", None)
        config["default_engine"] = g("TW2_DEFAULT_ENGINE", 'jinja')
        config["inject_resoures"] = g("TW2_INJECT_RESOURES", True)
        config["inject_resources_location"] = g("TW2_INJECT_RESOURCES_LOCATION", 'head')
        config["serve_resources"] = g("TW2_SERVE_RESOURCES", True)
        config["res_prefix"] = g("TW2_RES_PREFIX", '/tw2_resources/')
        config["res_max_age"] = g("TW2_RES_MAX_AGE", g("SEND_FILE_MAX_AGE_DEFAULT", 3600))
        config["serve_controllers"] = g("TW2_SERVE_CONTROLLERS", True)
        config["controller_prefix"] = g("TW2_CONTROLLER_PREFIX", '/tw2_controllers/')
        config["bufsize"] = g("TW2_BUFSIZE", 4096)
        config["params_as_vars"] = g("TW2_PARAMS_AS_VARS", False)
        config["debug"] = g("TW2_DEBUG", app.config["DEBUG"])
        config["validator_msgs"] = g("TW2_VALIDATOR_MSGS", {})
        config["encoding"] = g("TW2_ENCODING", 'utf-8')
        config["auto_reload_templates"] = g("TW2_AUTO_RELOAD_TEMPLATES", None)
        config["preferred_rendering_engines"] = g("TW2_PREFERRED_RENDERING_ENGINES", ['jinja', 'mako', 'genshi', 'kid', 'cheetah'])
        config["strict_engine_selection"] = g("TW2_STRICT_ENGINE_SELECTION", True)
        config["rendering_engine_lookup"] = g("TW2_RENDERING_ENGINE_LOOKUP", {'mako': 'mak', 'cheeta': 'tmpl', 'jinja': 'html', 'kid': 'kid'})
        config["script_name"] = g("TW2_SCRIPT_NAME", '')
        return config
        
    def register_resource(self, modname, filename, whole_dir):
        self.mw.resources.register(modname, filename, whole_dir)
    
    def register_controller(self, widget, path):
        self.mw.controllers.register(widget, path)
    
    def controller_url(self, name):
        return self.mw.config.controller_prefix+name

                          