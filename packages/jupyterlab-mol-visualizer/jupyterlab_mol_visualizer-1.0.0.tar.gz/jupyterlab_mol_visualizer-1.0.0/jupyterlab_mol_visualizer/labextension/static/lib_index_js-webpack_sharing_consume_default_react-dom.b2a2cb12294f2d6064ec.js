"use strict";
(self["webpackChunkjupyterlab_mol_visualizer"] = self["webpackChunkjupyterlab_mol_visualizer"] || []).push([["lib_index_js-webpack_sharing_consume_default_react-dom"],{

/***/ "./lib/icons.js":
/*!**********************!*\
  !*** ./lib/icons.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   molIcon: () => (/* binding */ molIcon)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _style_molecule_svg__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../style/molecule.svg */ "./style/molecule.svg");


const molIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'mol-icon',
    svgstr: _style_molecule_svg__WEBPACK_IMPORTED_MODULE_1__
});


/***/ }),

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
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/launcher */ "webpack/sharing/consume/default/@jupyterlab/launcher");
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./widget */ "./lib/widget.js");
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/filebrowser */ "webpack/sharing/consume/default/@jupyterlab/filebrowser");
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _icons__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./icons */ "./lib/icons.js");





/**
 * The command IDs used by the react-widget plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.create = 'create-react-widget';
})(CommandIDs || (CommandIDs = {}));
/**
 * Initialization data for the react-widget extension.
 */
const plugin = {
    id: 'jupyterlab_mol_visualizer:plugin',
    autoStart: true,
    optional: [_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1__.ILauncher, _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_2__.IDefaultFileBrowser, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.IThemeManager],
    activate: (app, launcher, browserFactory, themeManager) => {
        const { commands } = app;
        console.log('JupyterLab extension jupyterlab_mol_visualizer is activated!');
        const command = CommandIDs.create;
        commands.addCommand(command, {
            caption: 'Create a new React Widget',
            label: 'MOs Visualizer',
            icon: _icons__WEBPACK_IMPORTED_MODULE_3__.molIcon,
            execute: () => {
                var _a;
                let theme = 'dark';
                if ((_a = themeManager.theme) === null || _a === void 0 ? void 0 : _a.toLowerCase().includes('light')) {
                    theme = 'light';
                }
                else {
                    theme = 'dark';
                }
                const content = new _widget__WEBPACK_IMPORTED_MODULE_4__.CounterWidget(browserFactory, theme);
                const widget = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.MainAreaWidget({ content });
                // Watch for theme changes
                themeManager.themeChanged.connect((_, args) => {
                    const newTheme = args.newValue;
                    console.log(`Theme changed to: ${newTheme}`);
                    // Add your custom logic here
                });
                widget.title.label = 'MOL Visualizer';
                app.shell.add(widget, 'main');
            }
        });
        if (launcher) {
            launcher.add({
                command
            });
        }
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ }),

/***/ "./lib/inputs.js":
/*!***********************!*\
  !*** ./lib/inputs.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ Inputs)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _material_ui_core_styles__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @material-ui/core/styles */ "./node_modules/@material-ui/core/esm/styles/makeStyles.js");
/* harmony import */ var _material_ui_core_Paper__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @material-ui/core/Paper */ "./node_modules/@material-ui/core/esm/Paper/Paper.js");
/* harmony import */ var _material_ui_core_Divider__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @material-ui/core/Divider */ "./node_modules/@material-ui/core/esm/Divider/Divider.js");
/* harmony import */ var _material_ui_core_IconButton__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @material-ui/core/IconButton */ "./node_modules/@material-ui/core/esm/IconButton/IconButton.js");
/* harmony import */ var _material_ui_icons_Search__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @material-ui/icons/Search */ "./node_modules/@material-ui/icons/Search.js");
/* harmony import */ var _material_ui_lab_Autocomplete__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @material-ui/lab/Autocomplete */ "./node_modules/@material-ui/lab/esm/Autocomplete/Autocomplete.js");
/* harmony import */ var _material_ui_core_TextField__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @material-ui/core/TextField */ "./node_modules/@material-ui/core/esm/TextField/TextField.js");








const useStyles = (0,_material_ui_core_styles__WEBPACK_IMPORTED_MODULE_1__["default"])(theme => ({
    root: {
        padding: '2px 4px',
        display: 'flex',
        alignItems: 'center',
        width: 250,
        height: 30
    },
    input: {
        marginLeft: theme.spacing(1),
        flex: 1
    },
    iconButton: {
        padding: 10
    },
    divider: {
        height: 28,
        margin: 4
    }
}));
function Inputs(Props) {
    const classes = useStyles();
    const [value, setValue] = react__WEBPACK_IMPORTED_MODULE_0___default().useState(Props.options[0]);
    const [inputValue, setInputValue] = react__WEBPACK_IMPORTED_MODULE_0___default().useState('');
    const [files, setFiles] = react__WEBPACK_IMPORTED_MODULE_0___default().useState(Props.options);
    const handerClick = () => {
        Props.inputHandler(value);
    };
    Props.factory.model.pathChanged.connect((value) => {
        console.log('The path is changed: OK');
        const f = Props.getFiles(Props.types);
        setFiles(f);
        setValue(f[0]);
    });
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Paper__WEBPACK_IMPORTED_MODULE_2__["default"], { component: "form", className: classes.root },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_lab_Autocomplete__WEBPACK_IMPORTED_MODULE_3__["default"], { color: "primary", value: value, onChange: (event, newValue) => {
                    setValue(newValue);
                }, inputValue: inputValue, onInputChange: (event, newInputValue) => {
                    setInputValue(newInputValue);
                }, id: "controllable-states-demo", options: files, style: { width: 300, height: 50 }, renderInput: params => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_TextField__WEBPACK_IMPORTED_MODULE_4__["default"], { ...params, label: Props.label, variant: "outlined" })) }),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Divider__WEBPACK_IMPORTED_MODULE_5__["default"], { className: classes.divider, orientation: "vertical" }),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_IconButton__WEBPACK_IMPORTED_MODULE_6__["default"], { color: "primary", style: { height: 50 }, className: classes.iconButton, "aria-label": "directions", onClick: handerClick },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_icons_Search__WEBPACK_IMPORTED_MODULE_7__["default"], null)))));
}


/***/ }),

/***/ "./lib/sliders.js":
/*!************************!*\
  !*** ./lib/sliders.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ VerticalSlider)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _material_ui_core_styles__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @material-ui/core/styles */ "./node_modules/@material-ui/core/esm/styles/makeStyles.js");
/* harmony import */ var _material_ui_core_Slider__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @material-ui/core/Slider */ "./node_modules/@material-ui/core/esm/Slider/Slider.js");
/* harmony import */ var _material_ui_core_styles__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @material-ui/core/styles */ "./node_modules/@material-ui/core/esm/styles/createTheme.js");
/* harmony import */ var _material_ui_core_styles__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @material-ui/core/styles */ "./node_modules/@material-ui/styles/esm/ThemeProvider/ThemeProvider.js");
/* harmony import */ var _material_ui_core_CssBaseline__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @material-ui/core/CssBaseline */ "./node_modules/@material-ui/core/esm/CssBaseline/CssBaseline.js");
/* harmony import */ var _material_ui_core_Box__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @material-ui/core/Box */ "./node_modules/@material-ui/core/esm/Box/Box.js");
/* harmony import */ var _material_ui_core_Grid__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @material-ui/core/Grid */ "./node_modules/@material-ui/core/esm/Grid/Grid.js");
/* harmony import */ var _material_ui_core_Typography__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @material-ui/core/Typography */ "./node_modules/@material-ui/core/esm/Typography/Typography.js");








function VerticalSlider(Props) {
    const useStyles = (0,_material_ui_core_styles__WEBPACK_IMPORTED_MODULE_1__["default"])({
        root: {
            flexGrow: 1,
            marginTop: '40px',
            width: '900px',
            margin: '0 auto'
        }
    });
    function valuetext(value) {
        return `${value}°C`;
    }
    const marks2 = [
        {
            value: 0,
            label: '0'
        },
        {
            value: 0.01,
            label: '0.01'
        },
        {
            value: 0.02,
            label: '0.02'
        },
        {
            value: 0.03,
            label: '0.03'
        },
        {
            value: 0.04,
            label: '0.04'
        }
    ];
    const marks1 = [
        {
            value: 0,
            label: '0%'
        },
        {
            value: 20,
            label: '20%'
        },
        {
            value: 40,
            label: '40%'
        },
        {
            value: 60,
            label: '60%'
        },
        {
            value: 80,
            label: '80%'
        },
        {
            value: 100,
            label: '100%'
        }
    ];
    const classes = useStyles();
    // const prefersDarkMode = useMediaQuery('(prefers-color-scheme: dark)');
    const prefersDarkMode = Props.theme === 'dark' ? true : false;
    const theme = react__WEBPACK_IMPORTED_MODULE_0___default().useMemo(() => (0,_material_ui_core_styles__WEBPACK_IMPORTED_MODULE_2__["default"])({
        palette: {
            type: prefersDarkMode ? 'dark' : 'light'
        }
    }), [prefersDarkMode]);
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_styles__WEBPACK_IMPORTED_MODULE_3__["default"], { theme: theme },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_CssBaseline__WEBPACK_IMPORTED_MODULE_4__["default"], null),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: classes.root },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Grid__WEBPACK_IMPORTED_MODULE_5__["default"], { container: true, spacing: 3, justify: "center" },
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Grid__WEBPACK_IMPORTED_MODULE_5__["default"], { item: true, sm: 8 },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Box__WEBPACK_IMPORTED_MODULE_6__["default"], { id: Props.uuid, style: {
                                width: '600px',
                                height: '400px',
                                backgroundColor: 'black'
                            } })),
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Grid__WEBPACK_IMPORTED_MODULE_5__["default"], { item: true, sm: 1 },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Typography__WEBPACK_IMPORTED_MODULE_7__["default"], { id: "vertical-slider", gutterBottom: true }, "Transp."),
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Slider__WEBPACK_IMPORTED_MODULE_8__["default"], { style: { height: '350px' }, orientation: "vertical", getAriaValueText: valuetext, valueLabelDisplay: "on", defaultValue: 30, "aria-labelledby": "vertical-slider", min: 0, max: 100, marks: marks1, onChange: Props.changeHandler1, color: 'primary' })),
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Grid__WEBPACK_IMPORTED_MODULE_5__["default"], { item: true, sm: 1 },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Typography__WEBPACK_IMPORTED_MODULE_7__["default"], { id: "vertical-slider", gutterBottom: true }, "Isovalue"),
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Slider__WEBPACK_IMPORTED_MODULE_8__["default"], { style: { height: '350px' }, orientation: "vertical", defaultValue: 0.01, "aria-labelledby": "vertical-slider", getAriaValueText: valuetext, valueLabelDisplay: "on", marks: marks2, min: 0, max: 0.04, step: 0.001, onChange: Props.changeHandler2, color: 'secondary' })))))));
}


/***/ }),

/***/ "./lib/switches.js":
/*!*************************!*\
  !*** ./lib/switches.js ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ SwitchLabels)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _material_ui_core_FormGroup__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @material-ui/core/FormGroup */ "./node_modules/@material-ui/core/esm/FormGroup/FormGroup.js");
/* harmony import */ var _material_ui_core_FormControlLabel__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @material-ui/core/FormControlLabel */ "./node_modules/@material-ui/core/esm/FormControlLabel/FormControlLabel.js");
/* harmony import */ var _material_ui_core_Switch__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @material-ui/core/Switch */ "./node_modules/@material-ui/core/esm/Switch/Switch.js");
/* harmony import */ var _material_ui_core_styles__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @material-ui/core/styles */ "./node_modules/@material-ui/core/esm/styles/makeStyles.js");
/* harmony import */ var _material_ui_core_Grid__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @material-ui/core/Grid */ "./node_modules/@material-ui/core/esm/Grid/Grid.js");






function SwitchLabels(Props) {
    const useStyles = (0,_material_ui_core_styles__WEBPACK_IMPORTED_MODULE_1__["default"])(theme => ({
        container: {
            display: 'flex',
            flexWrap: 'wrap',
            position: 'absolute',
            top: 0,
            left: 0,
            height: '100%',
            width: '100%',
            alignItems: 'center'
        },
        textField: {
            marginLeft: theme.spacing(1),
            marginRight: theme.spacing(1),
            width: 200
        },
        formGroup: {
            alignItems: 'center'
        }
    }));
    const classes = useStyles();
    const [state, setState] = react__WEBPACK_IMPORTED_MODULE_0___default().useState({
        checkedA: false,
        checkedB: true,
        checkedC: true,
        checkedS: true,
        checkedI: true
    });
    const handleChange = (event) => {
        setState({ ...state, [event.target.name]: event.target.checked });
        if (event.target.name === 'checkedA') {
            Props.clickHandler1();
        }
        if (event.target.name === 'checkedB') {
            Props.clickHandler2();
        }
        if (event.target.name === 'checkedC') {
            Props.clickHandler3();
        }
    };
    const handleClick1 = () => {
        Props.bclick1();
        setState({
            checkedA: state.checkedA,
            checkedB: state.checkedB,
            checkedC: state.checkedC,
            checkedS: !state.checkedS,
            checkedI: state.checkedI
        });
    };
    const handleClick2 = () => {
        Props.bclick2();
        setState({
            checkedA: state.checkedA,
            checkedB: !state.checkedB,
            checkedC: !state.checkedC,
            checkedS: state.checkedS,
            checkedI: !state.checkedI
        });
    };
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Grid__WEBPACK_IMPORTED_MODULE_2__["default"], { container: true, spacing: 3, justifyContent: "center" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Grid__WEBPACK_IMPORTED_MODULE_2__["default"], { item: true, sm: 3 },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_FormControlLabel__WEBPACK_IMPORTED_MODULE_3__["default"], { control: react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Switch__WEBPACK_IMPORTED_MODULE_4__["default"], { checked: state.checkedS, onChange: handleClick1, name: "checkedS" }), label: "Show/hide structure" })),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Grid__WEBPACK_IMPORTED_MODULE_2__["default"], { item: true, sm: 3 },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_FormControlLabel__WEBPACK_IMPORTED_MODULE_3__["default"], { control: react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Switch__WEBPACK_IMPORTED_MODULE_4__["default"], { checked: state.checkedI, onChange: handleClick2, name: "checkedI" }), label: "Show/hide isosurface" }))),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Grid__WEBPACK_IMPORTED_MODULE_2__["default"], { container: true, justifyContent: "center" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_FormGroup__WEBPACK_IMPORTED_MODULE_5__["default"], { className: classes.formGroup, row: true },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_FormControlLabel__WEBPACK_IMPORTED_MODULE_3__["default"], { control: react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Switch__WEBPACK_IMPORTED_MODULE_4__["default"], { checked: state.checkedA, onChange: handleChange, name: "checkedA" }), label: "Auto-rotate" }),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_FormControlLabel__WEBPACK_IMPORTED_MODULE_3__["default"], { control: react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Switch__WEBPACK_IMPORTED_MODULE_4__["default"], { checked: state.checkedB, onChange: handleChange, name: "checkedB", color: "primary" }), label: "Positive isovalue" }),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_FormControlLabel__WEBPACK_IMPORTED_MODULE_3__["default"], { control: react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Switch__WEBPACK_IMPORTED_MODULE_4__["default"], { checked: state.checkedC, onChange: handleChange, name: "checkedC", color: "secondary" }), label: "Negative isovalue" })))));
}


/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   CounterWidget: () => (/* binding */ CounterWidget)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var ngl__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ngl */ "./node_modules/ngl/dist/ngl.esm.js");
/* harmony import */ var underscore__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! underscore */ "./node_modules/underscore/modules/index-all.js");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _sliders__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./sliders */ "./lib/sliders.js");
/* harmony import */ var _switches__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./switches */ "./lib/switches.js");
/* harmony import */ var _inputs__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./inputs */ "./lib/inputs.js");
/* harmony import */ var _material_ui_core_Grid__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @material-ui/core/Grid */ "./node_modules/@material-ui/core/esm/Grid/Grid.js");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _material_ui_core_Typography__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @material-ui/core/Typography */ "./node_modules/@material-ui/core/esm/Typography/Typography.js");











/**
 * A Counter Lumino Widget that wraps a CounterComponent.
 */
class CounterWidget extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ReactWidget {
    constructor(browserFactory, theme) {
        var _a;
        super();
        this.addClass('jp-ReactWidget');
        this.uuid = underscore__WEBPACK_IMPORTED_MODULE_3__.uniqueId('ngl_');
        this.theme = theme;
        this.browserFactory = browserFactory;
        this.currentDirectory = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_4__.URLExt.join(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_4__.PageConfig.getBaseUrl() + '/files', ((_a = this.browserFactory) === null || _a === void 0 ? void 0 : _a.model.path) + '/');
        window.requestAnimationFrame(() => {
            this.visualizer();
        });
        this.addStructure = this.addStructure.bind(this);
        this.addIsosurface = this.addIsosurface.bind(this);
        this.getCurrentDirectory = this.getCurrentDirectory.bind(this);
        this.updateDatasource = this.updateDatasource.bind(this);
        this.getFileList = this.getFileList.bind(this);
    }
    getCurrentDirectory() {
        var _a;
        this.currentDirectory = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_4__.URLExt.join(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_4__.PageConfig.getBaseUrl() + '/files', ((_a = this.browserFactory) === null || _a === void 0 ? void 0 : _a.model.path) + '/');
    }
    getFileList(types) {
        var _a;
        const a = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_5__.toArray)((_a = this.browserFactory) === null || _a === void 0 ? void 0 : _a.model.items());
        const b = a.filter(item => item.type === 'file' &&
            types.includes(item.name.split('.').pop()));
        const c = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_5__.map)(b, x => x.name);
        return (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_5__.toArray)(c);
    }
    updateDatasource() {
        this.getCurrentDirectory();
        ngl__WEBPACK_IMPORTED_MODULE_2__.DatasourceRegistry.add('data', new ngl__WEBPACK_IMPORTED_MODULE_2__.StaticDatasource(this.currentDirectory));
    }
    visualizer() {
        this.updateDatasource();
        if (this.theme === 'light') {
            this.stage = new ngl__WEBPACK_IMPORTED_MODULE_2__.Stage(this.uuid, { backgroundColor: 'white' });
        }
        else {
            this.stage = new ngl__WEBPACK_IMPORTED_MODULE_2__.Stage(this.uuid, { backgroundColor: 'black' });
        }
        window.addEventListener('resize', event => {
            this.stage.handleResize();
        }, false);
        this.stage.viewer.container.addEventListener('dblclick', () => {
            this.stage.toggleFullscreen();
        });
    }
    addStructure(filename) {
        this.updateDatasource();
        this.stage.getComponentsByName('structure1').forEach((element) => {
            this.stage.removeComponent(element);
        });
        this.stage
            .loadFile('data://' + filename, { name: 'structure1' })
            .then((o) => {
            o.addRepresentation('ball+stick');
            o.autoView();
        });
    }
    addIsosurface(filename) {
        this.updateDatasource();
        this.stage.getComponentsByName('surface_1').forEach((element) => {
            this.stage.removeComponent(element);
        });
        this.stage.getComponentsByName('surface_2').forEach((element) => {
            this.stage.removeComponent(element);
        });
        this.stage
            .loadFile('data://' + filename, { name: 'surface_1' })
            .then((o) => {
            o.addRepresentation('surface', {
                visible: true,
                isolevelType: 'value',
                isolevel: 0.01,
                color: 'blue',
                opacity: 0.7,
                opaqueBack: false
            });
            o.signals.visibilityChanged.add((value) => {
                console.log('visibility change to:' + value);
            });
            o.autoView();
        });
        this.stage
            .loadFile('data://' + filename, { name: 'surface_2' })
            .then((o) => {
            o.addRepresentation('surface', {
                visible: true,
                isolevelType: 'value',
                isolevel: -0.01,
                color: 'red',
                opacity: 0.7,
                opaqueBack: false
            });
            o.autoView();
        });
    }
    updateIsosurface(e) {
        this.stage
            .getRepresentationsByName('surface')
            .setParameters({ opacity: e });
        this.stage.getComponentsByName('surface_1').list[0].setVisibility(true);
        this.stage.getComponentsByName('surface_2').list[0].setVisibility(true);
    }
    updateIsolevel(e, filename) {
        this.stage
            .getComponentsByName(filename)
            .list[0].eachRepresentation((reprElem) => {
            reprElem.setParameters({ isolevel: e });
        });
    }
    toggleVisibility(filename) {
        const a = this.stage.getComponentsByName(filename).list[0];
        a.setVisibility(!a.visible);
    }
    setVisibility(filename, val) {
        const a = this.stage.getComponentsByName(filename).list[0];
        a.setVisibility(val);
    }
    toggleSpin() {
        this.stage.toggleSpin();
    }
    render() {
        const func1 = () => this.stage.toggleSpin();
        const func2 = () => this.toggleVisibility('surface_1');
        const func3 = () => this.toggleVisibility('surface_2');
        const bfunc1 = () => {
            this.toggleVisibility('structure1');
        };
        const bfunc2 = () => {
            this.toggleVisibility('surface_1');
            this.toggleVisibility('surface_2');
        };
        return (react__WEBPACK_IMPORTED_MODULE_1___default().createElement("div", null,
            react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_sliders__WEBPACK_IMPORTED_MODULE_6__["default"], { uuid: this.uuid, theme: this.theme, changeHandler1: (event, val) => {
                    const value = val / 100.0;
                    this.updateIsosurface(value);
                }, changeHandler2: (event, val) => {
                    const value = val;
                    this.updateIsolevel(value, 'surface_1');
                    this.updateIsolevel(-value, 'surface_2');
                } }),
            react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_material_ui_core_Grid__WEBPACK_IMPORTED_MODULE_7__["default"], { container: true, spacing: 3, justifyContent: "center" },
                react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_material_ui_core_Grid__WEBPACK_IMPORTED_MODULE_7__["default"], { item: true, sm: 3 },
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_inputs__WEBPACK_IMPORTED_MODULE_8__["default"], { getFiles: this.getFileList, types: ['sdf', 'cif'], factory: this.browserFactory, label: "Structure", options: this.getFileList(['sdf', 'cif']), inputHandler: this.addStructure })),
                react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_material_ui_core_Grid__WEBPACK_IMPORTED_MODULE_7__["default"], { item: true, sm: 3 },
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_inputs__WEBPACK_IMPORTED_MODULE_8__["default"], { getFiles: this.getFileList, types: ['cube'], factory: this.browserFactory, label: "Isosurface", options: this.getFileList(['cube']), inputHandler: this.addIsosurface }))),
            react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_switches__WEBPACK_IMPORTED_MODULE_9__["default"], { clickHandler1: func1, clickHandler2: func2, clickHandler3: func3, bclick1: bfunc1, bclick2: bfunc2 }),
            react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_material_ui_core_Typography__WEBPACK_IMPORTED_MODULE_10__["default"], { variant: "h6", align: "center" }, "Please select structure and Gaussian cube files from current directory to visualize.")));
    }
}


/***/ }),

/***/ "./style/molecule.svg":
/*!****************************!*\
  !*** ./style/molecule.svg ***!
  \****************************/
/***/ ((module) => {

module.exports = "<?xml version=\"1.0\" encoding=\"iso-8859-1\"?>\r\n<!-- Uploaded to: SVG Repo, www.svgrepo.com, Generator: SVG Repo Mixer Tools -->\r\n<svg height=\"800px\" width=\"800px\" version=\"1.1\" id=\"Layer_1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" \r\n\t viewBox=\"0 0 512 512\" xml:space=\"preserve\">\r\n<g>\r\n\t<path style=\"fill:#5CC4E0;\" d=\"M464.607,254.021c52.729,53.488,52.504,139.588-0.695,192.787\r\n\t\tc-53.434,53.434-140.058,53.434-193.492,0l3.453-3.453l190.04-190.029C464.158,253.562,464.372,253.786,464.607,254.021z\"/>\r\n\t<path style=\"fill:#5CC4E0;\" d=\"M238.128,443.355l3.453,3.453c-53.434,53.434-140.058,53.434-193.492,0\r\n\t\tc-53.199-53.199-53.424-139.299-0.695-192.787c0.235-0.235,0.46-0.47,0.695-0.705L238.128,443.355z\"/>\r\n</g>\r\n<g>\r\n\t<path style=\"fill:#439EE8;\" d=\"M238.128,443.355l-35.03-35.03c-46.847,46.847-119.201,52.618-172.338,17.323\r\n\t\tc4.964,7.475,10.738,14.57,17.328,21.16c53.434,53.434,140.058,53.434,193.492,0L238.128,443.355z\"/>\r\n\t<path style=\"fill:#439EE8;\" d=\"M273.872,443.355l35.03-35.03c46.847,46.847,119.201,52.618,172.338,17.323\r\n\t\tc-4.964,7.475-10.738,14.57-17.328,21.16c-53.434,53.434-140.058,53.434-193.492,0L273.872,443.355z\"/>\r\n</g>\r\n<path style=\"fill:#FF675C;\" d=\"M463.912,253.326l-190.04,190.029c-5.89,0.502-11.854,0.77-17.872,0.77\r\n\tc-6.018,0-11.982-0.267-17.872-0.77l-190.04-190.04c-0.235,0.235-0.46,0.47-0.695,0.705c-0.577-6.392-0.898-12.859-0.898-19.401\r\n\tc0-115.708,93.796-209.504,209.504-209.504s209.504,93.796,209.504,209.504c0,6.542-0.321,13.009-0.898,19.401\r\n\tC464.372,253.786,464.158,253.562,463.912,253.326z\"/>\r\n<path style=\"fill:#DB3D5A;\" d=\"M256,337.235c-97.236,0-178.987-66.242-202.615-156.059c-4.488,17.063-6.889,34.972-6.889,53.445\r\n\tc0,6.542,0.321,13.009,0.898,19.401c0.235-0.235,0.46-0.47,0.695-0.705l190.04,190.04c5.89,0.502,11.854,0.77,17.872,0.77\r\n\ts11.982-0.267,17.872-0.77l190.04-190.029c0.246,0.235,0.46,0.46,0.695,0.695c0.577-6.392,0.898-12.859,0.898-19.401\r\n\tc0-18.473-2.401-36.382-6.889-53.445C434.988,270.993,353.237,337.235,256,337.235z\"/>\r\n<g>\r\n\t<path style=\"fill:#FAEC8E;\" d=\"M114.905,363.958c8.85,0,16.033,7.183,16.033,16.034s-7.183,16.034-16.033,16.034H72.149\r\n\t\tc-8.85,0-16.034-7.183-16.034-16.034s7.183-16.034,16.034-16.034H114.905z\"/>\r\n\t<path style=\"fill:#FAEC8E;\" d=\"M444.127,363.958c8.85,0,16.034,7.183,16.034,16.034s-7.183,16.034-16.034,16.034h-42.756\r\n\t\tc-8.85,0-16.034-7.183-16.034-16.034s7.183-16.034,16.034-16.034H444.127z\"/>\r\n\t<path style=\"fill:#FAEC8E;\" d=\"M320.134,223.932c8.85,0,16.033,7.183,16.033,16.034s-7.183,16.034-16.033,16.034h-48.101v48.101\r\n\t\tc0,8.85-7.183,16.034-16.034,16.034c-8.85,0-16.033-7.183-16.033-16.034v-48.101h-48.101c-8.85,0-16.034-7.183-16.034-16.034\r\n\t\ts7.183-16.034,16.034-16.034h48.101v-43.825c0-8.85,7.183-16.034,16.033-16.034c8.85,0,16.034,7.183,16.034,16.034v43.825\r\n\t\tL320.134,223.932L320.134,223.932z\"/>\r\n</g>\r\n<path d=\"M472.883,251.065c0.416-5.581,0.638-11.099,0.638-16.444c0-119.941-97.58-217.521-217.521-217.521\r\n\tc-37.961,0-75.332,9.926-108.073,28.704c-31.752,18.211-58.622,44.357-77.705,75.611c-2.308,3.779-1.115,8.713,2.664,11.02\r\n\tc3.78,2.307,8.713,1.115,11.02-2.664C120.855,69.26,185.19,33.133,256,33.133c111.1,0,201.488,90.387,201.488,201.488\r\n\tc0,4.65-0.176,9.448-0.518,14.31L270.307,435.582c-4.803,0.342-9.603,0.525-14.307,0.525c-4.704,0-9.505-0.184-14.307-0.525\r\n\tL55.03,248.92c-0.341-4.859-0.517-9.653-0.517-14.3c0-23.296,3.939-46.123,11.706-67.848c1.491-4.169-0.681-8.756-4.85-10.248\r\n\tc-4.167-1.49-8.756,0.68-10.248,4.85c-8.389,23.461-12.642,48.105-12.642,73.245c0,5.344,0.222,10.863,0.638,16.444\r\n\tc-25.376,27.06-39.238,62.241-39.116,99.485c0.127,38.502,15.191,74.7,42.419,101.927c27.357,27.358,63.729,42.426,102.415,42.426\r\n\ts75.057-15.066,102.415-42.424c0.162-0.162,0.311-0.332,0.456-0.504c2.782,0.108,5.554,0.17,8.295,0.17s5.512-0.062,8.295-0.17\r\n\tc0.145,0.172,0.294,0.342,0.456,0.504c27.357,27.356,63.729,42.424,102.415,42.424s75.057-15.066,102.415-42.424\r\n\tC496.807,425.25,511.871,389.052,512,350.55C512.123,313.307,498.259,278.125,472.883,251.065z M53.758,441.14\r\n\tc-48.181-48.18-50.074-125.82-5.487-176.304l181.796,181.795c-23.551,20.842-53.516,32.237-85.233,32.237\r\n\tC110.432,478.868,78.087,465.468,53.758,441.14z M458.244,441.14c-24.329,24.328-56.674,37.728-91.078,37.728\r\n\tc-31.716,0-61.682-11.394-85.232-32.236l181.801-181.791C508.317,315.325,506.422,392.961,458.244,441.14z\"/>\r\n<path d=\"M256,156.056c-13.262,0-24.05,10.788-24.05,24.05v35.808h-40.084c-13.262,0-24.05,10.788-24.05,24.05\r\n\ts10.788,24.05,24.05,24.05h40.084v40.084c0,13.262,10.788,24.05,24.05,24.05c13.262,0,24.05-10.788,24.05-24.05v-40.084h40.084\r\n\tc13.262,0,24.05-10.788,24.05-24.05s-10.788-24.05-24.05-24.05h-40.084v-35.808C280.051,166.845,269.262,156.056,256,156.056z\r\n\t M320.134,231.948c4.421,0,8.017,3.596,8.017,8.017s-3.596,8.017-8.017,8.017h-48.101c-4.427,0-8.017,3.589-8.017,8.017v48.101\r\n\tc0,4.421-3.596,8.017-8.017,8.017c-4.421,0-8.017-3.596-8.017-8.017v-48.101c0-4.427-3.589-8.017-8.017-8.017h-48.101\r\n\tc-4.421,0-8.017-3.596-8.017-8.017s3.596-8.017,8.017-8.017h48.101c4.427,0,8.017-3.589,8.017-8.017v-43.825\r\n\tc0-4.421,3.596-8.017,8.017-8.017c4.421,0,8.017,3.596,8.017,8.017v43.825c0,4.427,3.589,8.017,8.017,8.017L320.134,231.948\r\n\tL320.134,231.948z\"/>\r\n<path d=\"M114.905,355.941H72.149c-13.262,0-24.05,10.788-24.05,24.05c0,13.262,10.788,24.05,24.05,24.05h42.756\r\n\tc13.262,0,24.05-10.788,24.05-24.05C138.956,366.729,128.167,355.941,114.905,355.941z M114.905,388.008H72.149\r\n\tc-4.421,0-8.017-3.596-8.017-8.017s3.596-8.017,8.017-8.017h42.756c4.421,0,8.017,3.596,8.017,8.017\r\n\tS119.326,388.008,114.905,388.008z\"/>\r\n<path d=\"M444.127,355.941h-42.756c-13.262,0-24.05,10.788-24.05,24.05c0,13.262,10.788,24.05,24.05,24.05h42.756\r\n\tc13.262,0,24.05-10.788,24.05-24.05C468.177,366.729,457.389,355.941,444.127,355.941z M444.127,388.008h-42.756\r\n\tc-4.421,0-8.017-3.596-8.017-8.017s3.596-8.017,8.017-8.017h42.756c4.421,0,8.017,3.596,8.017,8.017\r\n\tS448.548,388.008,444.127,388.008z\"/>\r\n<path d=\"M404.82,188.872c0.904,0,1.824-0.154,2.723-0.479c4.164-1.504,6.321-6.099,4.818-10.264\r\n\tc-1.325-3.67-2.798-7.335-4.377-10.894c-1.796-4.048-6.532-5.873-10.579-4.077s-5.873,6.532-4.077,10.579\r\n\tc1.426,3.214,2.756,6.525,3.953,9.838C398.459,186.841,401.539,188.872,404.82,188.872z\"/>\r\n<path d=\"M370.302,137.209c1.585,1.859,3.836,2.814,6.102,2.814c1.84,0,3.69-0.63,5.199-1.918c3.368-2.873,3.77-7.932,0.897-11.301\r\n\tC350.846,89.692,304.739,68.407,256,68.407c-4.427,0-8.017,3.589-8.017,8.017s3.589,8.017,8.017,8.017\r\n\tC300.038,84.44,341.699,103.674,370.302,137.209z\"/>\r\n</svg>";

/***/ })

}]);
//# sourceMappingURL=lib_index_js-webpack_sharing_consume_default_react-dom.b2a2cb12294f2d6064ec.js.map