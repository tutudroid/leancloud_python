<template>
 <div class="registerFormVue">
  <div class="form-group">
    <label for="account" class="col-sm-2 control-label">萌趣账号</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="account" v-model="username">
    </div>
  </div>
  <div class="form-group">
    <label for="password" class="col-sm-2 control-label">密码</label>
    <div class="col-sm-10">
      <input type="password" class="form-control" id="password" v-model="password">
    </div>
  </div>
  <div class="form-group">
    <label for="passwordSure" class="col-sm-2 control-label">确认密码</label>
    <div class="col-sm-10">
      <input type="password" class="form-control" id="passwordSure" v-model="passwordSure">
    </div>
  </div>
  <div class="form-group">
    <label for="phone" class="col-sm-2 control-label">手机号</label>
    <div class="col-sm-10">
      <input type="password" class="form-control" id="phone" v-model="phone">
    </div>
  </div>
  <div class="form-group">
    <label for="verifyCode" class="col-sm-2 control-label">验证码</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="verifyCode" v-model="verifyCode">
    </div>
  </div>
  <div class="form-group">
    <label for="pictureVerifyCode" class="col-sm-2 control-label">请输入右侧验证码</label>
    <div class="col-sm-10">
      	<div id="v_container" style="width: 200px;height: 50px;"></div>
      <input type="text" class="form-control" id="pictureVerifyCode" v-model="pictureVerifyCode">
    </div>
  </div>
  <span class="btn btn-default" @click="register()">注册</span>
 </div>
</template>

<script>
//generate verifyCode
!(function(window, document) {
	function GVerify(options) { //创建一个图形验证码对象，接收options对象为参数
		this.options = { //默认options参数值
			id: "", //容器Id
			type: "", //图形验证码类型 blend:数字字母混合类型、number:纯数字、letter:纯字母、equation算式
			canvasId: "verifyCanvas", //canvas的ID
			width: "100", //默认canvas宽度
			height: "30", //默认canvas高度
			code: ""

		}
		
		if(Object.prototype.toString.call(options) == "[object Object]"){//判断传入参数类型
			for(var i in options) { //根据传入的参数，修改默认参数值
				this.options[i] = options[i];
			}
		}else{
			this.options.id = options;
		}
		
		/** this.options.numArr = "0,1,2,3,4,5,6,7,8,9".split(","); **/
		/** this.options.equationOper = "+,-,*".split(","); **/
		/** this.options.letterArr = getAllLetter(); **/
		this.options.equationNum = "-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9".split(",");
		this.options.Equ = "";

		this._init();
		this.refresh();
	}

	GVerify.prototype = {
		/**版本号**/
		version: '1.0.0',
		
		/**初始化方法**/
		_init: function() {
			var con = document.getElementById(this.options.id);
			var canvas = document.createElement("canvas");
			this.options.width = con.offsetWidth > 0 ? con.offsetWidth : "100";
			this.options.height = con.offsetHeight > 0 ? con.offsetHeight : "30";
			canvas.id = this.options.canvasId;
			canvas.width = this.options.width;
			canvas.height = this.options.height;
			canvas.style.cursor = "pointer";
			canvas.innerHTML = "您的浏览器版本不支持canvas";
			con.appendChild(canvas);
			var parent = this;
			canvas.onclick = function(){
				parent.refresh();
			}
		},
		
		/**生成验证码**/
		refresh: function() {
			this.options.code = "";
			var canvas = document.getElementById(this.options.canvasId);
			if(canvas.getContext) {
				var ctx = canvas.getContext('2d');
			}else{
				return;
			}
			
			ctx.textBaseline = "middle";

			ctx.fillStyle = randomColor(180, 240);
			ctx.fillRect(0, 0, this.options.width, this.options.height);

			//判断验证码类型
			if (this.options.type == "blend") { 
				var txtArr = getBlend();
			} else if (this.options.type == "number") {
				var txtArr = getNumber();
			} else if (this.options.type=="letter") {
				var txtArr = getLetter();
			} else if (this.options.type="equation") {
				var txtArr = getEquation().split(",");
			}

			for(var i = 0; i < 4; i++) {
				var txt = txtArr[i];
				this.options.code += txt;
				this.options.Equ += txt+","
				ctx.font = randomNum(this.options.height/2, this.options.height) + 'px SimHei'; //随机生成字体大小
				ctx.fillStyle = randomColor(50, 160); //随机生成字体颜色		
				ctx.shadowOffsetX = randomNum(-3, 3);
				ctx.shadowOffsetY = randomNum(-3, 3);
				ctx.shadowBlur = randomNum(-3, 3);
				ctx.shadowColor = "rgba(0, 0, 0, 0.3)";
				var x = 25 + this.options.width / 5 * i;
				var y = this.options.height / 2;
				var deg = randomNum(-30, 30);
				/**设置旋转角度和坐标原点**/
				ctx.translate(x, y);
				ctx.rotate(deg * Math.PI / 180);
				ctx.fillText(txt, 0, 0);
				/**恢复旋转角度和坐标原点**/
				ctx.rotate(-deg * Math.PI / 180);
				ctx.translate(-x, -y);
			}
			/**绘制干扰线**/
			for(var i = 0; i < 4; i++) {
				ctx.strokeStyle = randomColor(40, 180);
				ctx.beginPath();
				ctx.moveTo(randomNum(0, this.options.width), randomNum(0, this.options.height));
				ctx.lineTo(randomNum(0, this.options.width), randomNum(0, this.options.height));
				ctx.stroke();
			}
			/**绘制干扰点**/
			for(var i = 0; i < this.options.width/4; i++) {
				ctx.fillStyle = randomColor(0, 255);
				ctx.beginPath();
				ctx.arc(randomNum(0, this.options.width), randomNum(0, this.options.height), 1, 0, 2 * Math.PI);
				ctx.fill();
			}
		},
		
		/**验证验证码**/
		validate: function(code){
			var code = code.toLowerCase();
			var v_code = this.options.code.toLowerCase();
			/** console.log(v_code); **/
			if(code == v_code){
				return true;
			}else{
				this.refresh();
				return false;
			}
		},

		/** 生成算式答案 **/
		validate4Equation: function(code){
			var txtArr = this.options.Equ.split(",");
			var num1 = parseInt(txtArr[0]);
			var num2 = parseInt(txtArr[2]);
			var op = txtArr[1];
			var ans=0;
			if (op=="+") {
				ans = num1+num2;
			}else if (op == "-"){
				ans = num1-num2;
			}else if (op == "*"){
				ans = num1*num2;
			}
			this.options.Equ = "";
			if (ans==code) {
				return true;
			}
			else {
				this.refresh();
				return false;
			}
		},
		/** 返回验证码类型 **/
		returnType: function(){
			return this.options.type;
		}
	}
	/**生成字母数组**/
	function getAllLetter() {
		var letterStr = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z";
		return letterStr.split(",");
	}
	/**生成一个随机数**/
	function randomNum(min, max) {
		return Math.floor(Math.random() * (max - min) + min);
	}
	/**生成一个随机色**/
	function randomColor(min, max) {
		var r = randomNum(min, max);
		var g = randomNum(min, max);
		var b = randomNum(min, max);
		return "rgb(" + r + "," + g + "," + b + ")";
	}
	/** 生成随机数学算式 **/
	function getEquation() {
		var num1 = randomNum(-9,9);
		var num2 = randomNum(-9,9);
		var equationOper = "+,-,*".split(",");
		var oper = equationOper[randomNum(0,equationOper.length)];
		var equal = "=";
		 return ""+num1+","+oper+","+num2+","+equal+""; 

	}
	/** 生成随机字符串 **/
	function getLetter(){
		var letArr = new Array();
		var letterArr = getAllLetter();
		for (var i=0; i < 4; i ++){
			letArr[i]=letterArr[randomNum(0,letterArr.length)];
		}
		return letArr; 
	}
	/** 生成随机数字串 **/
	function getNumber(){
		var numArr = new Array();
		for (var i = 0; i < 4; i ++){
			numArr[i] = randomNum(0,9);
		}
		return numArr;
	}
	/** 生成随机混合串 **/
	function getBlend(){
		var blendArr = new Array();
		var letterArr = getAllLetter();
		for (var i=0;i<4;i++){
			var flag = randomNum(0,2);
			if (flag==0){
				blendArr[i]=randomNum(0,9);
			}
			else {
				blendArr[i]=letterArr[randomNum(0,letterArr.length)];
			}
		}
		return blendArr;
	}

	window.GVerify = GVerify;
})(window, document);








                var verifyCode = new GVerify({id:"v_container",type:"blend"});
		document.getElementById("my_button").onclick = function(){
			// var res = verifyCode.validate(document.getElementById("code_input").value);
			
			var typee = verifyCode.returnType();
			if (typee == "equation"){
				var test = verifyCode.validate4Equation(document.getElementById("code_input").value);
				if(test){
					alert("验证正确");
				}else{
					alert("验证码错误");
				}
			}
			else {
				var res = verifyCode.validate(document.getElementById("code_input").value);
				if (res) {
					alert("验证正确");
				}else {
					alert("验证码错误");
				}
			}
		}


  export default{
    data:function(){
      return {
        username:"",
	password:"",
        passwordSure:"",
	phone:"",
	verifyCode:"",
	pictureVerifyCode:"",
	verifyCodeFromPhone:"",
      }
    },
    methods:{
      register(){
      
      },
    },
  }










