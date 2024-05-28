"use strict";
(self["webpackChunkcatppuccin_jupyterlab"] = self["webpackChunkcatppuccin_jupyterlab"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _palettes__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./palettes */ "./lib/palettes.js");



/**
 * Initialization data for the catppuccin_jupyterlab extension.
 */
const plugin = {
    id: 'catppuccin_jupyterlab:plugin',
    description: '📊 Soothing pastel theme for JupyterLab.',
    autoStart: true,
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.IThemeManager],
    optional: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__.ISettingRegistry],
    activate: (app, manager, settingRegistry) => {
        const style = 'catppuccin_jupyterlab/index.css';
        const palettes = new _palettes__WEBPACK_IMPORTED_MODULE_2__.CatppuccinPalettes();
        let brandColor = 'mauve';
        let accentColor = 'green';
        function loadSettings(settingRegistry) {
            if (settingRegistry) {
                settingRegistry
                    .load(plugin.id)
                    .then(settings => {
                    brandColor = settings.get('brandColor').composite;
                    accentColor = settings.get('accentColor').composite;
                    console.debug(`catppuccin_jupyterlab settings loaded. Brand color is '${brandColor}', Accent color is '${accentColor}'`);
                })
                    .catch(reason => {
                    console.error('Failed to load settings for catppuccin_jupyterlab.', reason);
                });
            }
        }
        loadSettings(settingRegistry);
        manager.register({
            name: 'Catppuccin Latte',
            isLight: true,
            load: () => {
                palettes.setColorsLatte();
                palettes.setConfigColors(brandColor, accentColor);
                return manager.loadCSS(style);
            },
            unload: () => Promise.resolve(undefined)
        });
        manager.register({
            name: 'Catppuccin Frappé',
            isLight: false,
            load: () => {
                palettes.setColorsFrappe();
                palettes.setConfigColors(brandColor, accentColor);
                return manager.loadCSS(style);
            },
            unload: () => Promise.resolve(undefined)
        });
        manager.register({
            name: 'Catppuccin Macchiato',
            isLight: false,
            load: () => {
                palettes.setColorsMacchiato();
                palettes.setConfigColors(brandColor, accentColor);
                return manager.loadCSS(style);
            },
            unload: () => Promise.resolve(undefined)
        });
        manager.register({
            name: 'Catppuccin Mocha',
            isLight: false,
            load: () => {
                palettes.setColorsMocha();
                palettes.setConfigColors(brandColor, accentColor);
                return manager.loadCSS(style);
            },
            unload: () => Promise.resolve(undefined)
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ }),

/***/ "./lib/palettes.js":
/*!*************************!*\
  !*** ./lib/palettes.js ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   CatppuccinPalettes: () => (/* binding */ CatppuccinPalettes)
/* harmony export */ });
class CatppuccinPalettes {
    setConfigColors(brandColor, accentColor) {
        document.documentElement.style.setProperty('--ctp-cfg-brand-color', `var(--ctp-plt-${brandColor})`);
        document.documentElement.style.setProperty('--ctp-cfg-accent-color', `var(--ctp-plt-${accentColor})`);
    }
    setColorsLatte() {
        document.documentElement.style.setProperty('--ctp-plt-rosewater', '#dc8a78');
        document.documentElement.style.setProperty('--ctp-plt-flamingo', '#dd7878');
        document.documentElement.style.setProperty('--ctp-plt-pink', '#ea76cb');
        document.documentElement.style.setProperty('--ctp-plt-mauve', '#8839ef');
        document.documentElement.style.setProperty('--ctp-plt-red', '#d20f39');
        document.documentElement.style.setProperty('--ctp-plt-maroon', '#e64553');
        document.documentElement.style.setProperty('--ctp-plt-peach', '#fe640b');
        document.documentElement.style.setProperty('--ctp-plt-yellow', '#df8e1d');
        document.documentElement.style.setProperty('--ctp-plt-green', '#40a02b');
        document.documentElement.style.setProperty('--ctp-plt-teal', '#179299');
        document.documentElement.style.setProperty('--ctp-plt-sky', '#04a5e5');
        document.documentElement.style.setProperty('--ctp-plt-sapphire', '#209fb5');
        document.documentElement.style.setProperty('--ctp-plt-blue', '#1e66f5');
        document.documentElement.style.setProperty('--ctp-plt-lavender', '#7287fd');
        document.documentElement.style.setProperty('--ctp-plt-text', '#4c4f69');
        document.documentElement.style.setProperty('--ctp-plt-subtext1', '#5c5f77');
        document.documentElement.style.setProperty('--ctp-plt-subtext0', '#6c6f85');
        document.documentElement.style.setProperty('--ctp-plt-overlay2', '#7c7f93');
        document.documentElement.style.setProperty('--ctp-plt-overlay1', '#8c8fa1');
        document.documentElement.style.setProperty('--ctp-plt-overlay0', '#9ca0b0');
        document.documentElement.style.setProperty('--ctp-plt-surface2', '#acb0be');
        document.documentElement.style.setProperty('--ctp-plt-surface1', '#bcc0cc');
        document.documentElement.style.setProperty('--ctp-plt-surface0', '#ccd0da');
        document.documentElement.style.setProperty('--ctp-plt-base', '#eff1f5');
        document.documentElement.style.setProperty('--ctp-plt-mantle', '#e6e9ef');
        document.documentElement.style.setProperty('--ctp-plt-crust', '#dce0e8');
    }
    setColorsFrappe() {
        document.documentElement.style.setProperty('--ctp-plt-rosewater', '#f2d5cf');
        document.documentElement.style.setProperty('--ctp-plt-flamingo', '#eebebe');
        document.documentElement.style.setProperty('--ctp-plt-pink', '#f4b8e4');
        document.documentElement.style.setProperty('--ctp-plt-mauve', '#ca9ee6');
        document.documentElement.style.setProperty('--ctp-plt-red', '#e78284');
        document.documentElement.style.setProperty('--ctp-plt-maroon', '#ea999c');
        document.documentElement.style.setProperty('--ctp-plt-peach', '#ef9f76');
        document.documentElement.style.setProperty('--ctp-plt-yellow', '#e5c890');
        document.documentElement.style.setProperty('--ctp-plt-green', '#a6d189');
        document.documentElement.style.setProperty('--ctp-plt-teal', '#81c8be');
        document.documentElement.style.setProperty('--ctp-plt-sky', '#99d1db');
        document.documentElement.style.setProperty('--ctp-plt-sapphire', '#85c1dc');
        document.documentElement.style.setProperty('--ctp-plt-blue', '#8caaee');
        document.documentElement.style.setProperty('--ctp-plt-lavender', '#babbf1');
        document.documentElement.style.setProperty('--ctp-plt-text', '#c6d0f5');
        document.documentElement.style.setProperty('--ctp-plt-subtext1', '#b5bfe2');
        document.documentElement.style.setProperty('--ctp-plt-subtext0', '#a5adce');
        document.documentElement.style.setProperty('--ctp-plt-overlay2', '#949cbb');
        document.documentElement.style.setProperty('--ctp-plt-overlay1', '#838ba7');
        document.documentElement.style.setProperty('--ctp-plt-overlay0', '#737994');
        document.documentElement.style.setProperty('--ctp-plt-surface2', '#626880');
        document.documentElement.style.setProperty('--ctp-plt-surface1', '#51576d');
        document.documentElement.style.setProperty('--ctp-plt-surface0', '#414559');
        document.documentElement.style.setProperty('--ctp-plt-base', '#303446');
        document.documentElement.style.setProperty('--ctp-plt-mantle', '#292c3c');
        document.documentElement.style.setProperty('--ctp-plt-crust', '#232634');
    }
    setColorsMacchiato() {
        document.documentElement.style.setProperty('--ctp-plt-rosewater', '#f4dbd6');
        document.documentElement.style.setProperty('--ctp-plt-flamingo', '#f0c6c6');
        document.documentElement.style.setProperty('--ctp-plt-pink', '#f5bde6');
        document.documentElement.style.setProperty('--ctp-plt-mauve', '#c6a0f6');
        document.documentElement.style.setProperty('--ctp-plt-red', '#ed8796');
        document.documentElement.style.setProperty('--ctp-plt-maroon', '#ee99a0');
        document.documentElement.style.setProperty('--ctp-plt-peach', '#f5a97f');
        document.documentElement.style.setProperty('--ctp-plt-yellow', '#eed49f');
        document.documentElement.style.setProperty('--ctp-plt-green', '#a6da95');
        document.documentElement.style.setProperty('--ctp-plt-teal', '#8bd5ca');
        document.documentElement.style.setProperty('--ctp-plt-sky', '#91d7e3');
        document.documentElement.style.setProperty('--ctp-plt-sapphire', '#7dc4e4');
        document.documentElement.style.setProperty('--ctp-plt-blue', '#8aadf4');
        document.documentElement.style.setProperty('--ctp-plt-lavender', '#b7bdf8');
        document.documentElement.style.setProperty('--ctp-plt-text', '#cad3f5');
        document.documentElement.style.setProperty('--ctp-plt-subtext1', '#b8c0e0');
        document.documentElement.style.setProperty('--ctp-plt-subtext0', '#a5adcb');
        document.documentElement.style.setProperty('--ctp-plt-overlay2', '#939ab7');
        document.documentElement.style.setProperty('--ctp-plt-overlay1', '#8087a2');
        document.documentElement.style.setProperty('--ctp-plt-overlay0', '#6e738d');
        document.documentElement.style.setProperty('--ctp-plt-surface2', '#5b6078');
        document.documentElement.style.setProperty('--ctp-plt-surface1', '#494d64');
        document.documentElement.style.setProperty('--ctp-plt-surface0', '#363a4f');
        document.documentElement.style.setProperty('--ctp-plt-base', '#24273a');
        document.documentElement.style.setProperty('--ctp-plt-mantle', '#1e2030');
        document.documentElement.style.setProperty('--ctp-plt-crust', '#181926');
    }
    setColorsMocha() {
        document.documentElement.style.setProperty('--ctp-plt-rosewater', '#f5e0dc');
        document.documentElement.style.setProperty('--ctp-plt-flamingo', '#f2cdcd');
        document.documentElement.style.setProperty('--ctp-plt-pink', '#f5c2e7');
        document.documentElement.style.setProperty('--ctp-plt-mauve', '#cba6f7');
        document.documentElement.style.setProperty('--ctp-plt-red', '#f38ba8');
        document.documentElement.style.setProperty('--ctp-plt-maroon', '#eba0ac');
        document.documentElement.style.setProperty('--ctp-plt-peach', '#fab387');
        document.documentElement.style.setProperty('--ctp-plt-yellow', '#f9e2af');
        document.documentElement.style.setProperty('--ctp-plt-green', '#a6e3a1');
        document.documentElement.style.setProperty('--ctp-plt-teal', '#94e2d5');
        document.documentElement.style.setProperty('--ctp-plt-sky', '#89dceb');
        document.documentElement.style.setProperty('--ctp-plt-sapphire', '#74c7ec');
        document.documentElement.style.setProperty('--ctp-plt-blue', '#89b4fa');
        document.documentElement.style.setProperty('--ctp-plt-lavender', '#b4befe');
        document.documentElement.style.setProperty('--ctp-plt-text', '#cdd6f4');
        document.documentElement.style.setProperty('--ctp-plt-subtext1', '#bac2de');
        document.documentElement.style.setProperty('--ctp-plt-subtext0', '#a6adc8');
        document.documentElement.style.setProperty('--ctp-plt-overlay2', '#9399b2');
        document.documentElement.style.setProperty('--ctp-plt-overlay1', '#7f849c');
        document.documentElement.style.setProperty('--ctp-plt-overlay0', '#6c7086');
        document.documentElement.style.setProperty('--ctp-plt-surface2', '#585b70');
        document.documentElement.style.setProperty('--ctp-plt-surface1', '#45475a');
        document.documentElement.style.setProperty('--ctp-plt-surface0', '#313244');
        document.documentElement.style.setProperty('--ctp-plt-base', '#1e1e2e');
        document.documentElement.style.setProperty('--ctp-plt-mantle', '#181825');
        document.documentElement.style.setProperty('--ctp-plt-crust', '#11111b');
    }
}


/***/ })

}]);
//# sourceMappingURL=lib_index_js.727d9d94804e7e034752.js.map