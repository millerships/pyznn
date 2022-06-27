"use strict";(self.webpackChunkwebsite=self.webpackChunkwebsite||[]).push([[80],{3905:(e,t,n)=>{n.d(t,{Zo:()=>s,kt:()=>d});var r=n(7294);function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function a(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function l(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?a(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):a(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function o(e,t){if(null==e)return{};var n,r,i=function(e,t){if(null==e)return{};var n,r,i={},a=Object.keys(e);for(r=0;r<a.length;r++)n=a[r],t.indexOf(n)>=0||(i[n]=e[n]);return i}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)n=a[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(i[n]=e[n])}return i}var p=r.createContext({}),u=function(e){var t=r.useContext(p),n=t;return e&&(n="function"==typeof e?e(t):l(l({},t),e)),n},s=function(e){var t=u(e.components);return r.createElement(p.Provider,{value:t},e.children)},c={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},m=r.forwardRef((function(e,t){var n=e.components,i=e.mdxType,a=e.originalType,p=e.parentName,s=o(e,["components","mdxType","originalType","parentName"]),m=u(n),d=i,v=m["".concat(p,".").concat(d)]||m[d]||c[d]||a;return n?r.createElement(v,l(l({ref:t},s),{},{components:n})):r.createElement(v,l({ref:t},s))}));function d(e,t){var n=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var a=n.length,l=new Array(a);l[0]=m;var o={};for(var p in t)hasOwnProperty.call(t,p)&&(o[p]=t[p]);o.originalType=e,o.mdxType="string"==typeof e?e:i,l[1]=o;for(var u=2;u<a;u++)l[u]=n[u];return r.createElement.apply(null,l)}return r.createElement.apply(null,n)}m.displayName="MDXCreateElement"},1933:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>p,contentTitle:()=>l,default:()=>c,frontMatter:()=>a,metadata:()=>o,toc:()=>u});var r=n(7462),i=(n(7294),n(3905));const a={sidebar_position:5},l="Contributing",o={unversionedId:"contributing",id:"contributing",title:"Contributing",description:"If you want to contribute to this repo and looking for directions, follow along.",source:"@site/docs/contributing.md",sourceDirName:".",slug:"/contributing",permalink:"/pyznn/docs/contributing",draft:!1,editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/contributing.md",tags:[],version:"current",sidebarPosition:5,frontMatter:{sidebar_position:5},sidebar:"tutorialSidebar",previous:{title:"Wallet",permalink:"/pyznn/docs/wallet"}},p={},u=[{value:"Setting up local dev",id:"setting-up-local-dev",level:2},{value:"Pre-requisites",id:"pre-requisites",level:3},{value:"Configure local development environment",id:"configure-local-development-environment",level:3},{value:"Running Tests",id:"running-tests",level:3},{value:"Raising PR",id:"raising-pr",level:2},{value:"Deploying documentation",id:"deploying-documentation",level:2}],s={toc:u};function c(e){let{components:t,...n}=e;return(0,i.kt)("wrapper",(0,r.Z)({},s,n,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"contributing"},"Contributing"),(0,i.kt)("p",null,"If you want to contribute to this repo and looking for directions, follow along."),(0,i.kt)("h2",{id:"setting-up-local-dev"},"Setting up local dev"),(0,i.kt)("h3",{id:"pre-requisites"},"Pre-requisites"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"Python 3.8.10 (preferred)")),(0,i.kt)("p",null,"We suggest using ",(0,i.kt)("a",{parentName:"p",href:"https://github.com/pyenv/pyenv-virtualenv"},(0,i.kt)("inlineCode",{parentName:"a"},"pyenv"))," to easily manage python versions. Some of the following commands use ",(0,i.kt)("inlineCode",{parentName:"p"},"pyenv"),".\nUse ",(0,i.kt)("a",{parentName:"p",href:"https://github.com/pyenv/pyenv-installer"},"pyenv-installer")," for easy installation. Then add pyenv-virtualenv plugin to it."),(0,i.kt)("h3",{id:"configure-local-development-environment"},"Configure local development environment"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Install and activate python 3.8.10 in the root directory"),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"pyenv install 3.8.10")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"pyenv virtualenv 3.8.10 pyznn")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"pyenv local pyznn")))),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Install dev requirements"),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},'pip install -e ".[dev]"')))),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Install precommit hook"),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"pre-commit install"))))),(0,i.kt)("p",null,"You're all set to hack!"),(0,i.kt)("p",null,"Before making changes, let's ensure tests run successfully on local."),(0,i.kt)("h3",{id:"running-tests"},"Running Tests"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"Run all tests with coverage",(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"coverage run -m pytest -v")))),(0,i.kt)("li",{parentName:"ul"},"Show report in terminal",(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"coverage report -m"))))),(0,i.kt)("h2",{id:"raising-pr"},"Raising PR"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"Please fork this repo and push changes to your own feature branch"),(0,i.kt)("li",{parentName:"ul"},"Ensure that tests are covered"),(0,i.kt)("li",{parentName:"ul"},"Update the documentation website (markdown)"),(0,i.kt)("li",{parentName:"ul"},"Open a PR for review by core-team")),(0,i.kt)("h2",{id:"deploying-documentation"},"Deploying documentation"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"USE_SSH=true GITHUB_HOST=github.com-roymiller yarn deploy\n")))}c.isMDXComponent=!0}}]);