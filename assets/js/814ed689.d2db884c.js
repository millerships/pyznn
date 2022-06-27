"use strict";(self.webpackChunkwebsite=self.webpackChunkwebsite||[]).push([[52],{3905:(e,t,r)=>{r.d(t,{Zo:()=>s,kt:()=>u});var n=r(7294);function a(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function i(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function o(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?i(Object(r),!0).forEach((function(t){a(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):i(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function l(e,t){if(null==e)return{};var r,n,a=function(e,t){if(null==e)return{};var r,n,a={},i=Object.keys(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var p=n.createContext({}),c=function(e){var t=n.useContext(p),r=t;return e&&(r="function"==typeof e?e(t):o(o({},t),e)),r},s=function(e){var t=c(e.components);return n.createElement(p.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},f=n.forwardRef((function(e,t){var r=e.components,a=e.mdxType,i=e.originalType,p=e.parentName,s=l(e,["components","mdxType","originalType","parentName"]),f=c(r),u=a,m=f["".concat(p,".").concat(u)]||f[u]||d[u]||i;return r?n.createElement(m,o(o({ref:t},s),{},{components:r})):n.createElement(m,o({ref:t},s))}));function u(e,t){var r=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var i=r.length,o=new Array(i);o[0]=f;var l={};for(var p in t)hasOwnProperty.call(t,p)&&(l[p]=t[p]);l.originalType=e,l.mdxType="string"==typeof e?e:a,o[1]=l;for(var c=2;c<i;c++)o[c]=r[c];return n.createElement.apply(null,o)}return n.createElement.apply(null,r)}f.displayName="MDXCreateElement"},1314:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>p,contentTitle:()=>o,default:()=>d,frontMatter:()=>i,metadata:()=>l,toc:()=>c});var n=r(7462),a=(r(7294),r(3905));const i={sidebar_position:4},o="Wallet",l={unversionedId:"wallet",id:"wallet",title:"Wallet",description:"Create wallet from mnemonic",source:"@site/docs/wallet.md",sourceDirName:".",slug:"/wallet",permalink:"/docs/wallet",draft:!1,editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/wallet.md",tags:[],version:"current",sidebarPosition:4,frontMatter:{sidebar_position:4},sidebar:"tutorialSidebar",previous:{title:"Built-in APIs",permalink:"/docs/api"},next:{title:"Contributing",permalink:"/docs/contributing"}},p={},c=[{value:"Create wallet from mnemonic",id:"create-wallet-from-mnemonic",level:2},{value:"Get Keypair from PrivateKey",id:"get-keypair-from-privatekey",level:2},{value:"Signing and verifying a message",id:"signing-and-verifying-a-message",level:2}],s={toc:c};function d(e){let{components:t,...r}=e;return(0,a.kt)("wrapper",(0,n.Z)({},s,r,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"wallet"},"Wallet"),(0,a.kt)("h2",{id:"create-wallet-from-mnemonic"},"Create wallet from mnemonic"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},'from znn.wallet.keystore import KeyStore\n\nMNEMONIC = (\n    "route become dream access impulse price inform obtain engage ski believe awful "\n    "absent pig thing vibrant possible exotic flee pepper marble rural fire fancy"\n)\n\nkeystore = KeyStore(MNEMONIC)\n\nprint(keystore.seed)\n# Out: 19f1d107d49f42ebc14d46b51001c731569f142590fdd20167ddeedbb201516731ad5ac9b58d3a1c9c09debfe62538379461e4ea9f038124c428784fecc645b7\n\nkp = keystore.get_key_pair(0)  # `0` is default btw, so no need to pass it, just being explicit here for the sake of the example\n\nprint(kp.private_key)\n# Out: d6b01f96b566d7df9b5b53b1971e4baeb74cc64167a9843f82d04b2194ca4863\n\nprint(str(kp.address))\n# Out: z1qqjnwjjpnue8xmmpanz6csze6tcmtzzdtfsww7\n')),(0,a.kt)("p",null,"Following BIP44, ",(0,a.kt)("inlineCode",{parentName:"p"},"m / purpose' / coin_type' / account' / change / address_index"),", you can get keypairs for other account indices as well."),(0,a.kt)("p",null,"For example, ",(0,a.kt)("inlineCode",{parentName:"p"},"kp = keystore.get_key_pair(1)")," works."),(0,a.kt)("h2",{id:"get-keypair-from-privatekey"},"Get Keypair from PrivateKey"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},'from znn.wallet.keypair import KeyPair\n\nkeypair = KeyPair("d6b01f96b566d7df9b5b53b1971e4baeb74cc64167a9843f82d04b2194ca4863")\n\nprint(str(keypair.address))\n# Out: z1qqjnwjjpnue8xmmpanz6csze6tcmtzzdtfsww7\n')),(0,a.kt)("h2",{id:"signing-and-verifying-a-message"},"Signing and verifying a message"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre"},'from znn.wallet.keypair import KeyPair\nfrom znn.wallet.keypair import verify_signature\n\nkeypair = KeyPair("d6b01f96b566d7df9b5b53b1971e4baeb74cc64167a9843f82d04b2194ca4863")\n\nsigned_msg = keypair.sign("Hello, aliens")\nverify_signature(keypair.public_key, signed_msg.decode(), "Hello, aliens")\n')),(0,a.kt)("p",null,"Verification throws ",(0,a.kt)("inlineCode",{parentName:"p"},"BadSignatureError")," if it fails."))}d.isMDXComponent=!0}}]);