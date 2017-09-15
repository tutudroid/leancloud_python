<template>
	<div class="selfcenterPwdVue">
		<div class="changePwd">
		  <div class="control-group">
		    <label class="control-label">原密码</label>
		    <div class="controls">
		      <input type="originPwd" id="originPwd" v-model="originPwd">
		    </div>
		  </div>
		  <div class="control-group">
		    <label class="control-label" for="passqord" >新密码</label>
		    <div class="controls">
		      <input type="password" id="password" v-model="newPwd">
		    </div>
		  </div>
		  <div class="control-group">
		    <label class="control-label" for="confirmPassword">确认密码</label>
		    <div class="controls">
		      <input type="password" id="confirmPassword" v-model="confirmPwd">
		    </div>
		  </div>
		  <div class="control-group">
		    <div class="controls">
		      <span class="btn myBtn" @click="changePwd()">确认</span>
		    </div>
		  </div>
		</div>
	</div>
</template>
<script>
	export default{
		data:function(){
			return {
				originPwd:"",
				newPwd:"",
				confirmPwd:"",
			}
		},
		methods:{
			changePwd(){
				let current = $("xx").attr("id");
				swal(
				   {
				     title:"你确定要修改密码吗？",
				     text:"",
				     type:"warning",
				     showCancelButton:true,
				     closeOnConfirm:false,
				     confirmButtonText:"是的，我要修改它",
				     confirmButtonColor:"ec6c62",
				   },function(){
					$.ajax({
						type: 'xx',
						url: '/xx/xx/',
						data: {
						    'objectId': current,
						    'originPwd':state, 
						    'newPwd':newPwd,
						    'confirmPwd':confirmPwd,
						    'csrfmiddlewaretoken': $('#csrfProductManager input[name="csrfmiddlewaretoken"]').prop('value')
						},
						success: function (data) {
						  swal('修改成功');
						},
			      	    error: function(XMLHttpRequest, textStatus, errorThrown) {
				          swal("修改失败");
				        },
					});
				});
			}
		}
	}
</script>