"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[2168,2200],{92168:(e,t,n)=>{n.r(t),n.d(t,{CommandRegistry:()=>d});var i,r=n(39296),s=n(11296),o=n(48832),a=n(96296),l=n(72200),c=n(43884);class d{constructor(){this._timerID=0,this._replaying=!1,this._keystrokes=[],this._keydownEvents=[],this._keyBindings=[],this._exactKeyMatch=null,this._commands=new Map,this._commandChanged=new c.Signal(this),this._commandExecuted=new c.Signal(this),this._keyBindingChanged=new c.Signal(this)}get commandChanged(){return this._commandChanged}get commandExecuted(){return this._commandExecuted}get keyBindingChanged(){return this._keyBindingChanged}get keyBindings(){return this._keyBindings}listCommands(){return Array.from(this._commands.keys())}hasCommand(e){return this._commands.has(e)}addCommand(e,t){if(this._commands.has(e))throw new Error(`Command '${e}' already registered.`);return this._commands.set(e,i.createCommand(t)),this._commandChanged.emit({id:e,type:"added"}),new o.DisposableDelegate((()=>{this._commands.delete(e),this._commandChanged.emit({id:e,type:"removed"})}))}notifyCommandChanged(e){if(void 0!==e&&!this._commands.has(e))throw new Error(`Command '${e}' is not registered.`);this._commandChanged.emit({id:e,type:e?"changed":"many-changed"})}describedBy(e,t=s.JSONExt.emptyObject){var n;let i=this._commands.get(e);return Promise.resolve(null!==(n=null==i?void 0:i.describedBy.call(void 0,t))&&void 0!==n?n:{args:null})}label(e,t=s.JSONExt.emptyObject){var n;let i=this._commands.get(e);return null!==(n=null==i?void 0:i.label.call(void 0,t))&&void 0!==n?n:""}mnemonic(e,t=s.JSONExt.emptyObject){let n=this._commands.get(e);return n?n.mnemonic.call(void 0,t):-1}icon(e,t=s.JSONExt.emptyObject){var n;return null===(n=this._commands.get(e))||void 0===n?void 0:n.icon.call(void 0,t)}iconClass(e,t=s.JSONExt.emptyObject){let n=this._commands.get(e);return n?n.iconClass.call(void 0,t):""}iconLabel(e,t=s.JSONExt.emptyObject){let n=this._commands.get(e);return n?n.iconLabel.call(void 0,t):""}caption(e,t=s.JSONExt.emptyObject){let n=this._commands.get(e);return n?n.caption.call(void 0,t):""}usage(e,t=s.JSONExt.emptyObject){let n=this._commands.get(e);return n?n.usage.call(void 0,t):""}className(e,t=s.JSONExt.emptyObject){let n=this._commands.get(e);return n?n.className.call(void 0,t):""}dataset(e,t=s.JSONExt.emptyObject){let n=this._commands.get(e);return n?n.dataset.call(void 0,t):{}}isEnabled(e,t=s.JSONExt.emptyObject){let n=this._commands.get(e);return!!n&&n.isEnabled.call(void 0,t)}isToggled(e,t=s.JSONExt.emptyObject){let n=this._commands.get(e);return!!n&&n.isToggled.call(void 0,t)}isToggleable(e,t=s.JSONExt.emptyObject){let n=this._commands.get(e);return!!n&&n.isToggleable}isVisible(e,t=s.JSONExt.emptyObject){let n=this._commands.get(e);return!!n&&n.isVisible.call(void 0,t)}execute(e,t=s.JSONExt.emptyObject){let n,i=this._commands.get(e);if(!i)return Promise.reject(new Error(`Command '${e}' not registered.`));try{n=i.execute.call(void 0,t)}catch(e){n=Promise.reject(e)}let r=Promise.resolve(n);return this._commandExecuted.emit({id:e,args:t,result:r}),r}addKeyBinding(e){let t=i.createKeyBinding(e);return this._keyBindings.push(t),this._keyBindingChanged.emit({binding:t,type:"added"}),new o.DisposableDelegate((()=>{r.ArrayExt.removeFirstOf(this._keyBindings,t),this._keyBindingChanged.emit({binding:t,type:"removed"})}))}processKeydownEvent(e){if(this._replaying||d.isModifierKeyPressed(e))return;let t=d.keystrokeForKeydownEvent(e);if(!t)return this._replayKeydownEvents(),void this._clearPendingState();this._keystrokes.push(t);let{exact:n,partial:r}=i.matchKeyBinding(this._keyBindings,this._keystrokes,e);return n||r?(e.preventDefault(),e.stopPropagation(),n&&!r?(this._executeKeyBinding(n),void this._clearPendingState()):(n&&(this._exactKeyMatch=n),this._keydownEvents.push(e),void this._startTimer())):(this._replayKeydownEvents(),void this._clearPendingState())}_startTimer(){this._clearTimer(),this._timerID=window.setTimeout((()=>{this._onPendingTimeout()}),i.CHORD_TIMEOUT)}_clearTimer(){0!==this._timerID&&(clearTimeout(this._timerID),this._timerID=0)}_replayKeydownEvents(){0!==this._keydownEvents.length&&(this._replaying=!0,this._keydownEvents.forEach(i.replayKeyEvent),this._replaying=!1)}_executeKeyBinding(e){let{command:t,args:n}=e,i={_luminoEvent:{type:"keybinding",keys:e.keys},...n};if(this.hasCommand(t)&&this.isEnabled(t,i))this.execute(t,i);else{let n=this.hasCommand(t)?"enabled":"registered",i=`Cannot execute key binding '${e.keys.join(", ")}':`,r=`command '${t}' is not ${n}.`;console.warn(`${i} ${r}`)}}_clearPendingState(){this._clearTimer(),this._exactKeyMatch=null,this._keystrokes.length=0,this._keydownEvents.length=0}_onPendingTimeout(){this._timerID=0,this._exactKeyMatch?this._executeKeyBinding(this._exactKeyMatch):this._replayKeydownEvents(),this._clearPendingState()}}!function(e){function t(e){let t="",n=!1,i=!1,r=!1,s=!1;for(let o of e.split(/\s+/))"Accel"===o?a.Platform.IS_MAC?i=!0:r=!0:"Alt"===o?n=!0:"Cmd"===o?i=!0:"Ctrl"===o?r=!0:"Shift"===o?s=!0:o.length>0&&(t=o);return{cmd:i,ctrl:r,alt:n,shift:s,key:t}}function n(e){let n="",i=t(e);return i.ctrl&&(n+="Ctrl "),i.alt&&(n+="Alt "),i.shift&&(n+="Shift "),i.cmd&&a.Platform.IS_MAC&&(n+="Cmd "),n+i.key}e.parseKeystroke=t,e.normalizeKeystroke=n,e.normalizeKeys=function(e){let t;return t=a.Platform.IS_WIN?e.winKeys||e.keys:a.Platform.IS_MAC?e.macKeys||e.keys:e.linuxKeys||e.keys,t.map(n)},e.formatKeystroke=function(e){return"string"==typeof e?n(e):e.map(n).join(", ");function n(e){let n=[],r=a.Platform.IS_MAC?" ":"+",s=t(e);return s.ctrl&&n.push("Ctrl"),s.alt&&n.push("Alt"),s.shift&&n.push("Shift"),a.Platform.IS_MAC&&s.cmd&&n.push("Cmd"),n.push(s.key),n.map(i.formatKey).join(r)}},e.isModifierKeyPressed=function(e){let t=(0,l.Cs)(),n=t.keyForKeydownEvent(e);return t.isModifierKey(n)},e.keystrokeForKeydownEvent=function(e){let t=(0,l.Cs)(),n=t.keyForKeydownEvent(e);if(!n||t.isModifierKey(n))return"";let i=[];return e.ctrlKey&&i.push("Ctrl"),e.altKey&&i.push("Alt"),e.shiftKey&&i.push("Shift"),e.metaKey&&a.Platform.IS_MAC&&i.push("Cmd"),i.push(n),i.join(" ")}}(d||(d={})),function(e){e.CHORD_TIMEOUT=1e3,e.createCommand=function(e){return{execute:e.execute,describedBy:h("function"==typeof e.describedBy?e.describedBy:{args:null,...e.describedBy},(()=>({args:null}))),label:h(e.label,i),mnemonic:h(e.mnemonic,r),icon:h(e.icon,m),iconClass:h(e.iconClass,i),iconLabel:h(e.iconLabel,i),caption:h(e.caption,i),usage:h(e.usage,i),className:h(e.className,i),dataset:h(e.dataset,c),isEnabled:e.isEnabled||o,isToggled:e.isToggled||l,isToggleable:e.isToggleable||!!e.isToggled,isVisible:e.isVisible||o}},e.createKeyBinding=function(e){return{keys:d.normalizeKeys(e),selector:y(e),command:e.command,args:e.args||s.JSONExt.emptyObject}},e.matchKeyBinding=function(e,t,n){let i=null,r=!1,s=1/0,o=0;for(let l=0,c=e.length;l<c;++l){let c=e[l],d=u(c.keys,t);if(0===d)continue;if(2===d){r||-1===g(c.selector,n)||(r=!0);continue}let m=g(c.selector,n);if(-1===m||m>s)continue;let h=a.Selector.calculateSpecificity(c.selector);(!i||m<s||h>=o)&&(i=c,s=m,o=h)}return{exact:i,partial:r}},e.replayKeyEvent=function(e){e.target.dispatchEvent(function(e){let t=document.createEvent("Event"),n=e.bubbles||!0,i=e.cancelable||!0;return t.initEvent(e.type||"keydown",n,i),t.key=e.key||"",t.keyCode=e.keyCode||0,t.which=e.keyCode||0,t.ctrlKey=e.ctrlKey||!1,t.altKey=e.altKey||!1,t.shiftKey=e.shiftKey||!1,t.metaKey=e.metaKey||!1,t.view=e.view||window,t}(e))},e.formatKey=function(e){return a.Platform.IS_MAC?t.hasOwnProperty(e)?t[e]:e:n.hasOwnProperty(e)?n[e]:e};const t={Backspace:"⌫",Tab:"⇥",Enter:"⏎",Shift:"⇧",Ctrl:"⌃",Alt:"⌥",Escape:"⎋",PageUp:"⇞",PageDown:"⇟",End:"↘",Home:"↖",ArrowLeft:"←",ArrowUp:"↑",ArrowRight:"→",ArrowDown:"↓",Delete:"⌦",Cmd:"⌘"},n={Escape:"Esc",PageUp:"Page Up",PageDown:"Page Down",ArrowLeft:"Left",ArrowUp:"Up",ArrowRight:"Right",ArrowDown:"Down",Delete:"Del"},i=()=>"",r=()=>-1,o=()=>!0,l=()=>!1,c=()=>({}),m=()=>{};function h(e,t){return void 0===e?t:"function"==typeof e?e:()=>e}function y(e){if(-1!==e.selector.indexOf(","))throw new Error(`Selector cannot contain commas: ${e.selector}`);if(!a.Selector.isValid(e.selector))throw new Error(`Invalid selector: ${e.selector}`);return e.selector}function u(e,t){if(e.length<t.length)return 0;for(let n=0,i=t.length;n<i;++n)if(e[n]!==t[n])return 0;return e.length>t.length?2:1}function g(e,t){let n=t.target,i=t.currentTarget;for(let t=0;null!==n;n=n.parentElement,++t){if(n.hasAttribute("data-lm-suppress-shortcuts"))return-1;if(a.Selector.matches(n,e))return t;if(n===i)return-1}return-1}}(i||(i={}))},72200:(e,t,n)=>{function i(){return o.keyboardLayout}n.d(t,{Cs:()=>i});class r{constructor(e,t,n=[]){this.name=e,this._codes=t,this._keys=r.extractKeys(t),this._modifierKeys=r.convertToKeySet(n)}keys(){return Object.keys(this._keys)}isValidKey(e){return e in this._keys}isModifierKey(e){return e in this._modifierKeys}keyForKeydownEvent(e){return this._codes[e.keyCode]||""}}!function(e){e.extractKeys=function(e){let t=Object.create(null);for(let n in e)t[e[n]]=!0;return t},e.convertToKeySet=function(e){let t=Object(null);for(let n=0,i=e.length;n<i;++n)t[e[n]]=!0;return t}}(r||(r={}));const s=new r("en-us",{8:"Backspace",9:"Tab",13:"Enter",16:"Shift",17:"Ctrl",18:"Alt",19:"Pause",27:"Escape",32:"Space",33:"PageUp",34:"PageDown",35:"End",36:"Home",37:"ArrowLeft",38:"ArrowUp",39:"ArrowRight",40:"ArrowDown",45:"Insert",46:"Delete",48:"0",49:"1",50:"2",51:"3",52:"4",53:"5",54:"6",55:"7",56:"8",57:"9",59:";",61:"=",65:"A",66:"B",67:"C",68:"D",69:"E",70:"F",71:"G",72:"H",73:"I",74:"J",75:"K",76:"L",77:"M",78:"N",79:"O",80:"P",81:"Q",82:"R",83:"S",84:"T",85:"U",86:"V",87:"W",88:"X",89:"Y",90:"Z",91:"Meta",93:"ContextMenu",96:"0",97:"1",98:"2",99:"3",100:"4",101:"5",102:"6",103:"7",104:"8",105:"9",106:"*",107:"+",109:"-",110:".",111:"/",112:"F1",113:"F2",114:"F3",115:"F4",116:"F5",117:"F6",118:"F7",119:"F8",120:"F9",121:"F10",122:"F11",123:"F12",173:"-",186:";",187:"=",188:",",189:"-",190:".",191:"/",192:"`",219:"[",220:"\\",221:"]",222:"'",224:"Meta"},["Shift","Ctrl","Alt","Meta"]);var o;!function(e){e.keyboardLayout=s}(o||(o={}))}}]);