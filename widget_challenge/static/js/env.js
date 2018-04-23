// http://www.jvandemo.com/how-to-configure-your-angularjs-application-using-environment-variables/

'use strict';
window.__env = window.__env || {};

// API url
window.__env.api_url = 'http://localhost';

// port
window.__env.port = 8000;

// Base url
window.__env.base_url = '/';

// Whether or not to enable debug mode
// Setting this to false will disable console output
window.__env.enable_debug = true;
