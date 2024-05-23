"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[9780,9272],{39780:function(t,e,r){var n,o=this&&this.__extends||(n=function(t,e){return n=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var r in e)Object.prototype.hasOwnProperty.call(e,r)&&(t[r]=e[r])},n(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function r(){this.constructor=t}n(t,e),t.prototype=null===e?Object.create(e):(r.prototype=e.prototype,new r)}),i=this&&this.__assign||function(){return i=Object.assign||function(t){for(var e,r=1,n=arguments.length;r<n;r++)for(var o in e=arguments[r])Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o]);return t},i.apply(this,arguments)},a=this&&this.__read||function(t,e){var r="function"==typeof Symbol&&t[Symbol.iterator];if(!r)return t;var n,o,i=r.call(t),a=[];try{for(;(void 0===e||e-- >0)&&!(n=i.next()).done;)a.push(n.value)}catch(t){o={error:t}}finally{try{n&&!n.done&&(r=i.return)&&r.call(i)}finally{if(o)throw o.error}}return a},l=this&&this.__spreadArray||function(t,e,r){if(r||2===arguments.length)for(var n,o=0,i=e.length;o<i;o++)!n&&o in e||(n||(n=Array.prototype.slice.call(e,0,o)),n[o]=e[o]);return t.concat(n||Array.prototype.slice.call(e))},s=this&&this.__values||function(t){var e="function"==typeof Symbol&&Symbol.iterator,r=e&&t[e],n=0;if(r)return r.call(t);if(t&&"number"==typeof t.length)return{next:function(){return t&&n>=t.length&&(t=void 0),{value:t&&t[n++],done:!t}}};throw new TypeError(e?"Object is not iterable.":"Symbol.iterator is not defined.")};Object.defineProperty(e,"__esModule",{value:!0}),e.SafeHandler=e.SafeMathDocumentMixin=void 0;var f=r(82144);function c(t){var e;return e=function(t){function e(){for(var e,r,n=[],o=0;o<arguments.length;o++)n[o]=arguments[o];var i=t.apply(this,l([],a(n),!1))||this;i.safe=new i.options.SafeClass(i,i.options.safeOptions);var f=i.constructor.ProcessBits;f.has("safe")||f.allocate("safe");try{for(var c=s(i.inputJax),u=c.next();!u.done;u=c.next()){var p=u.value;p.name.match(/MathML/)?(p.mathml.filterAttribute=i.safe.mmlAttribute.bind(i.safe),p.mathml.filterClassList=i.safe.mmlClassList.bind(i.safe)):p.name.match(/TeX/)&&p.postFilters.add(i.sanitize.bind(p),-5.5)}}catch(t){e={error:t}}finally{try{u&&!u.done&&(r=c.return)&&r.call(c)}finally{if(e)throw e.error}}return i}return o(e,t),e.prototype.sanitize=function(t){t.math.root=this.parseOptions.root,t.document.safe.sanitize(t.math,t.document)},e}(t),e.OPTIONS=i(i({},t.OPTIONS),{safeOptions:i({},f.Safe.OPTIONS),SafeClass:f.Safe}),e}e.SafeMathDocumentMixin=c,e.SafeHandler=function(t){return t.documentClass=c(t.documentClass),t}},9052:function(t,e,r){var n=this&&this.__values||function(t){var e="function"==typeof Symbol&&Symbol.iterator,r=e&&t[e],n=0;if(r)return r.call(t);if(t&&"number"==typeof t.length)return{next:function(){return t&&n>=t.length&&(t=void 0),{value:t&&t[n++],done:!t}}};throw new TypeError(e?"Object is not iterable.":"Symbol.iterator is not defined.")},o=this&&this.__read||function(t,e){var r="function"==typeof Symbol&&t[Symbol.iterator];if(!r)return t;var n,o,i=r.call(t),a=[];try{for(;(void 0===e||e-- >0)&&!(n=i.next()).done;)a.push(n.value)}catch(t){o={error:t}}finally{try{n&&!n.done&&(r=i.return)&&r.call(i)}finally{if(o)throw o.error}}return a};Object.defineProperty(e,"__esModule",{value:!0}),e.SafeMethods=void 0;var i=r(40592);e.SafeMethods={filterURL:function(t,e){var r=(e.match(/^\s*([a-z]+):/i)||[null,""])[1].toLowerCase(),n=t.allow.URLs;return"all"===n||"safe"===n&&(t.options.safeProtocols[r]||!r)?e:null},filterClassList:function(t,e){var r=this;return e.trim().replace(/\s\s+/g," ").split(/ /).map((function(e){return r.filterClass(t,e)||""})).join(" ").trim().replace(/\s\s+/g,"")},filterClass:function(t,e){var r=t.allow.classes;return"all"===r||"safe"===r&&e.match(t.options.classPattern)?e:null},filterID:function(t,e){var r=t.allow.cssIDs;return"all"===r||"safe"===r&&e.match(t.options.idPattern)?e:null},filterStyles:function(t,e){var r,o,i,a;if("all"===t.allow.styles)return e;if("safe"!==t.allow.styles)return null;var l=t.adaptor,s=t.options;try{var f=l.node("div",{style:e}),c=l.node("div");try{for(var u=n(Object.keys(s.safeStyles)),p=u.next();!p.done;p=u.next()){var h=p.value;if(s.styleParts[h])try{for(var y=(i=void 0,n(["Top","Right","Bottom","Left"])),d=y.next();!d.done;d=y.next()){var v,m=h+d.value;(v=this.filterStyle(t,m,f))&&l.setStyle(c,m,v)}}catch(t){i={error:t}}finally{try{d&&!d.done&&(a=y.return)&&a.call(y)}finally{if(i)throw i.error}}else(v=this.filterStyle(t,h,f))&&l.setStyle(c,h,v)}}catch(t){r={error:t}}finally{try{p&&!p.done&&(o=u.return)&&o.call(u)}finally{if(r)throw r.error}}e=l.allStyles(c)}catch(t){e=""}return e},filterStyle:function(t,e,r){var n=t.adaptor.getStyle(r,e);if("string"!=typeof n||""===n||n.match(/^\s*calc/)||n.match(/javascript:/)&&!t.options.safeProtocols.javascript||n.match(/data:/)&&!t.options.safeProtocols.data)return null;var o=e.replace(/Top|Right|Left|Bottom/,"");return t.options.safeStyles[e]||t.options.safeStyles[o]?this.filterStyleValue(t,e,n,r):null},filterStyleValue:function(t,e,r,n){var o=t.options.styleLengths[e];if(!o)return r;if("string"!=typeof o)return this.filterStyleLength(t,e,r);var i=this.filterStyleLength(t,o,t.adaptor.getStyle(n,o));return i?(t.adaptor.setStyle(n,o,i),t.adaptor.getStyle(n,e)):null},filterStyleLength:function(t,e,r){if(!r.match(/^(.+)(em|ex|ch|rem|px|mm|cm|in|pt|pc|%)$/))return null;var n=(0,i.length2em)(r,1),a=t.options.styleLengths[e],l=o(Array.isArray(a)?a:[-t.options.lengthMax,t.options.lengthMax],2),s=l[0],f=l[1];return s<=n&&n<=f?r:(n<s?s:f).toFixed(3).replace(/\.?0+$/,"")+"em"},filterFontSize:function(t,e){return this.filterStyleLength(t,"fontSize",e)},filterSizeMultiplier:function(t,e){var r=o(t.options.scriptsizemultiplierRange||[-1/0,1/0],2),n=r[0],i=r[1];return Math.min(i,Math.max(n,parseFloat(e))).toString()},filterScriptLevel:function(t,e){var r=o(t.options.scriptlevelRange||[-1/0,1/0],2),n=r[0],i=r[1];return Math.min(i,Math.max(n,parseInt(e))).toString()},filterData:function(t,e,r){return r.match(t.options.dataPattern)?e:null}}},82144:function(t,e,r){var n=this&&this.__assign||function(){return n=Object.assign||function(t){for(var e,r=1,n=arguments.length;r<n;r++)for(var o in e=arguments[r])Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o]);return t},n.apply(this,arguments)},o=this&&this.__values||function(t){var e="function"==typeof Symbol&&Symbol.iterator,r=e&&t[e],n=0;if(r)return r.call(t);if(t&&"number"==typeof t.length)return{next:function(){return t&&n>=t.length&&(t=void 0),{value:t&&t[n++],done:!t}}};throw new TypeError(e?"Object is not iterable.":"Symbol.iterator is not defined.")};Object.defineProperty(e,"__esModule",{value:!0}),e.Safe=void 0;var i=r(69272),a=r(9052),l=function(){function t(t,e){this.filterAttributes=new Map([["href","filterURL"],["src","filterURL"],["altimg","filterURL"],["class","filterClassList"],["style","filterStyles"],["id","filterID"],["fontsize","filterFontSize"],["mathsize","filterFontSize"],["scriptminsize","filterFontSize"],["scriptsizemultiplier","filterSizeMultiplier"],["scriptlevel","filterScriptLevel"],["data-","filterData"]]),this.filterMethods=n({},a.SafeMethods),this.adaptor=t.adaptor,this.options=e,this.allow=this.options.allow}return t.prototype.sanitize=function(t,e){try{t.root.walkTree(this.sanitizeNode.bind(this))}catch(r){e.options.compileError(e,t,r)}},t.prototype.sanitizeNode=function(t){var e,r,n=t.attributes.getAllAttributes();try{for(var i=o(Object.keys(n)),a=i.next();!a.done;a=i.next()){var l=a.value,s=this.filterAttributes.get(l);if(s){var f=this.filterMethods[s](this,n[l]);f?f!==("number"==typeof f?parseFloat(n[l]):n[l])&&(n[l]=f):delete n[l]}}}catch(t){e={error:t}}finally{try{a&&!a.done&&(r=i.return)&&r.call(i)}finally{if(e)throw e.error}}},t.prototype.mmlAttribute=function(t,e){if("class"===t)return null;var r=this.filterAttributes.get(t)||("data-"===t.substr(0,5)?this.filterAttributes.get("data-"):null);if(!r)return e;var n=this.filterMethods[r](this,e,t);return"number"==typeof n||"boolean"==typeof n?String(n):n},t.prototype.mmlClassList=function(t){var e=this;return t.map((function(t){return e.filterMethods.filterClass(e,t)})).filter((function(t){return null!==t}))},t.OPTIONS={allow:{URLs:"safe",classes:"safe",cssIDs:"safe",styles:"safe"},lengthMax:3,scriptsizemultiplierRange:[.6,1],scriptlevelRange:[-2,2],classPattern:/^mjx-[-a-zA-Z0-9_.]+$/,idPattern:/^mjx-[-a-zA-Z0-9_.]+$/,dataPattern:/^data-mjx-/,safeProtocols:(0,i.expandable)({http:!0,https:!0,file:!0,javascript:!1,data:!1}),safeStyles:(0,i.expandable)({color:!0,backgroundColor:!0,border:!0,cursor:!0,margin:!0,padding:!0,textShadow:!0,fontFamily:!0,fontSize:!0,fontStyle:!0,fontWeight:!0,opacity:!0,outline:!0}),styleParts:(0,i.expandable)({border:!0,padding:!0,margin:!0,outline:!0}),styleLengths:(0,i.expandable)({borderTop:"borderTopWidth",borderRight:"borderRightWidth",borderBottom:"borderBottomWidth",borderLeft:"borderLeftWidth",paddingTop:!0,paddingRight:!0,paddingBottom:!0,paddingLeft:!0,marginTop:!0,marginRight:!0,marginBottom:!0,marginLeft:!0,outlineTop:!0,outlineRight:!0,outlineBottom:!0,outlineLeft:!0,fontSize:[.707,1.44]})},t}();e.Safe=l},69272:function(t,e){var r=this&&this.__values||function(t){var e="function"==typeof Symbol&&Symbol.iterator,r=e&&t[e],n=0;if(r)return r.call(t);if(t&&"number"==typeof t.length)return{next:function(){return t&&n>=t.length&&(t=void 0),{value:t&&t[n++],done:!t}}};throw new TypeError(e?"Object is not iterable.":"Symbol.iterator is not defined.")},n=this&&this.__read||function(t,e){var r="function"==typeof Symbol&&t[Symbol.iterator];if(!r)return t;var n,o,i=r.call(t),a=[];try{for(;(void 0===e||e-- >0)&&!(n=i.next()).done;)a.push(n.value)}catch(t){o={error:t}}finally{try{n&&!n.done&&(r=i.return)&&r.call(i)}finally{if(o)throw o.error}}return a},o=this&&this.__spreadArray||function(t,e,r){if(r||2===arguments.length)for(var n,o=0,i=e.length;o<i;o++)!n&&o in e||(n||(n=Array.prototype.slice.call(e,0,o)),n[o]=e[o]);return t.concat(n||Array.prototype.slice.call(e))};Object.defineProperty(e,"__esModule",{value:!0}),e.lookup=e.separateOptions=e.selectOptionsFromKeys=e.selectOptions=e.userOptions=e.defaultOptions=e.insert=e.copy=e.keys=e.makeArray=e.expandable=e.Expandable=e.OPTIONS=e.REMOVE=e.APPEND=e.isObject=void 0;var i={}.constructor;function a(t){return"object"==typeof t&&null!==t&&(t.constructor===i||t.constructor===l)}e.isObject=a,e.APPEND="[+]",e.REMOVE="[-]",e.OPTIONS={invalidOption:"warn",optionError:function(t,r){if("fatal"===e.OPTIONS.invalidOption)throw new Error(t);console.warn("MathJax: "+t)}};var l=function(){};function s(t){return Object.assign(Object.create(l.prototype),t)}function f(t){return t?Object.keys(t).concat(Object.getOwnPropertySymbols(t)):[]}function c(t){var e,n,o={};try{for(var i=r(f(t)),p=i.next();!p.done;p=i.next()){var h=p.value,y=Object.getOwnPropertyDescriptor(t,h),d=y.value;Array.isArray(d)?y.value=u([],d,!1):a(d)&&(y.value=c(d)),y.enumerable&&(o[h]=y)}}catch(t){e={error:t}}finally{try{p&&!p.done&&(n=i.return)&&n.call(i)}finally{if(e)throw e.error}}return Object.defineProperties(t.constructor===l?s({}):{},o)}function u(t,i,s){var p,h;void 0===s&&(s=!0);var y=function(r){if(s&&void 0===t[r]&&t.constructor!==l)return"symbol"==typeof r&&(r=r.toString()),e.OPTIONS.optionError('Invalid option "'.concat(r,'" (no default value).'),r),"continue";var p=i[r],h=t[r];if(!a(p)||null===h||"object"!=typeof h&&"function"!=typeof h)Array.isArray(p)?(t[r]=[],u(t[r],p,!1)):a(p)?t[r]=c(p):t[r]=p;else{var y=f(p);Array.isArray(h)&&(1===y.length&&(y[0]===e.APPEND||y[0]===e.REMOVE)&&Array.isArray(p[y[0]])||2===y.length&&y.sort().join(",")===e.APPEND+","+e.REMOVE&&Array.isArray(p[e.APPEND])&&Array.isArray(p[e.REMOVE]))?(p[e.REMOVE]&&(h=t[r]=h.filter((function(t){return p[e.REMOVE].indexOf(t)<0}))),p[e.APPEND]&&(t[r]=o(o([],n(h),!1),n(p[e.APPEND]),!1))):u(h,p,s)}};try{for(var d=r(f(i)),v=d.next();!v.done;v=d.next())y(v.value)}catch(t){p={error:t}}finally{try{v&&!v.done&&(h=d.return)&&h.call(d)}finally{if(p)throw p.error}}return t}function p(t){for(var e,n,o=[],i=1;i<arguments.length;i++)o[i-1]=arguments[i];var a={};try{for(var l=r(o),s=l.next();!s.done;s=l.next()){var f=s.value;t.hasOwnProperty(f)&&(a[f]=t[f])}}catch(t){e={error:t}}finally{try{s&&!s.done&&(n=l.return)&&n.call(l)}finally{if(e)throw e.error}}return a}e.Expandable=l,e.expandable=s,e.makeArray=function(t){return Array.isArray(t)?t:[t]},e.keys=f,e.copy=c,e.insert=u,e.defaultOptions=function(t){for(var e=[],r=1;r<arguments.length;r++)e[r-1]=arguments[r];return e.forEach((function(e){return u(t,e,!1)})),t},e.userOptions=function(t){for(var e=[],r=1;r<arguments.length;r++)e[r-1]=arguments[r];return e.forEach((function(e){return u(t,e,!0)})),t},e.selectOptions=p,e.selectOptionsFromKeys=function(t,e){return p.apply(void 0,o([t],n(Object.keys(e)),!1))},e.separateOptions=function(t){for(var e,n,o,i,a=[],l=1;l<arguments.length;l++)a[l-1]=arguments[l];var s=[];try{for(var f=r(a),c=f.next();!c.done;c=f.next()){var u=c.value,p={},h={};try{for(var y=(o=void 0,r(Object.keys(t||{}))),d=y.next();!d.done;d=y.next()){var v=d.value;(void 0===u[v]?h:p)[v]=t[v]}}catch(t){o={error:t}}finally{try{d&&!d.done&&(i=y.return)&&i.call(y)}finally{if(o)throw o.error}}s.push(p),t=h}}catch(t){e={error:t}}finally{try{c&&!c.done&&(n=f.return)&&n.call(f)}finally{if(e)throw e.error}}return s.unshift(t),s},e.lookup=function(t,e,r){return void 0===r&&(r=null),e.hasOwnProperty(t)?e[t]:r}},40592:(t,e)=>{Object.defineProperty(e,"__esModule",{value:!0}),e.px=e.emRounded=e.em=e.percent=e.length2em=e.MATHSPACE=e.RELUNITS=e.UNITS=e.BIGDIMEN=void 0,e.BIGDIMEN=1e6,e.UNITS={px:1,in:96,cm:96/2.54,mm:96/25.4},e.RELUNITS={em:1,ex:.431,pt:.1,pc:1.2,mu:1/18},e.MATHSPACE={veryverythinmathspace:1/18,verythinmathspace:2/18,thinmathspace:3/18,mediummathspace:4/18,thickmathspace:5/18,verythickmathspace:6/18,veryverythickmathspace:7/18,negativeveryverythinmathspace:-1/18,negativeverythinmathspace:-2/18,negativethinmathspace:-3/18,negativemediummathspace:-4/18,negativethickmathspace:-5/18,negativeverythickmathspace:-6/18,negativeveryverythickmathspace:-7/18,thin:.04,medium:.06,thick:.1,normal:1,big:2,small:1/Math.sqrt(2),infinity:e.BIGDIMEN},e.length2em=function(t,r,n,o){if(void 0===r&&(r=0),void 0===n&&(n=1),void 0===o&&(o=16),"string"!=typeof t&&(t=String(t)),""===t||null==t)return r;if(e.MATHSPACE[t])return e.MATHSPACE[t];var i=t.match(/^\s*([-+]?(?:\.\d+|\d+(?:\.\d*)?))?(pt|em|ex|mu|px|pc|in|mm|cm|%)?/);if(!i)return r;var a=parseFloat(i[1]||"1"),l=i[2];return e.UNITS.hasOwnProperty(l)?a*e.UNITS[l]/o/n:e.RELUNITS.hasOwnProperty(l)?a*e.RELUNITS[l]:"%"===l?a/100*r:a*r},e.percent=function(t){return(100*t).toFixed(1).replace(/\.?0+$/,"")+"%"},e.em=function(t){return Math.abs(t)<.001?"0":t.toFixed(3).replace(/\.?0+$/,"")+"em"},e.emRounded=function(t,e){return void 0===e&&(e=16),t=(Math.round(t*e)+.05)/e,Math.abs(t)<.001?"0em":t.toFixed(3).replace(/\.?0+$/,"")+"em"},e.px=function(t,r,n){return void 0===r&&(r=-e.BIGDIMEN),void 0===n&&(n=16),t*=n,r&&t<r&&(t=r),Math.abs(t)<.1?"0":t.toFixed(1).replace(/\.0$/,"")+"px"}}}]);