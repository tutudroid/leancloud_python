<template>
<div class="systemAccountVue">

<table class="table table-striped one shown" v-if="allsysusers.length > 0">
<thead>	
  <tr class="success">
    <td>用户名ddd</td>
    <td>角色</td>
    <td>状态</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</thead>

<tbody>
    <tr v-for="sysUser in allsysusers" class="accountRow"><td>{{sysUser.username}}</td><td>{{sysUser.role[0]}}</td><td v-if="sysUser.forbidden">禁用</td><td v-else>正常</td><td :class="['link',sysUser.forbidden == false?'forbid':'restore']" @click="forbid($event,sysUser.objectId)" v-if="sysUser.forbidden!=true">禁用</td><td :class="['link',sysUser.forbidden == true?'restore':'false']" @click="forbid($event,sysUser.objectId)" v-if="sysUser.forbidden">恢复</td><td class="link" @click="hide(sysUser.objectId)">修改密码</td><td class="link" @click="deleteUser($event,sysUser.objectId)">删除</td></tr>
</tbody>
</table>

<div class="changePwd hide">
	  <div class="control-group">
	    <label class="control-label" for="uniqueId" ></label>
	    <div class="controls">
	      <input type="text" id="uniqueId" v-model="uniqueId" hidden>
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
	      <span class="btn myBtn" @click="hide()">取消</span>
	    </div>
	  </div>
</div>

</div>
</template>


<script>
  export default {
      data: function(){
        return {
	  uniqueId : "",
	  newPwd : "",
	  confirmPwd : "",
	  id:"",
	}
      },
      props:['allsysusers'],
      methods: {
        hide(id=0){
		  this.id = id;
		  var hidden = $('.hide');
		  var shown =  $('.shown');
		  if(hidden != null){
		  hidden.removeClass("hide").addClass('shown');
		  }
		  if(shown !=null){
		  shown.removeClass('shown').addClass('hide');
		  }
		},
       changePwd(){
	        $.ajax({
	            type: 'POST',
	            url: '/Admin/ResetUserPassword/',
	            data: {
	                'objectId': this.id,
	                'password': this.newPwd,
		            'passwordSure':this.confirmPwd,
	                'csrfmiddlewaretoken': $('#csrfProductManager input[name="csrfmiddlewaretoken"]').prop('value')
	            },
	            success: function (data) {
	      			swal("您的密码已经被修改");
	            },
	            error: function(XMLHttpRequest, textStatus, errorThrown) {
	     			swal("您的密码修改失败");
	            },
	       	});
       },
       forbid(event,id){
	 var forbid = $(event.target);
	 let state = forbid.attr('class').slice(5);
	 console.log(state=="forbid");
	 if(state == "forbid"){
	 swal(
	   {
	     title:"你确定禁用它吗？",
	     text:"禁用之后此账号将无法使用",
	     type:"warning",
	     showCancelButton:true,
	     closeOnConfirm:false,
	     confirmButtonText:"是的，我要禁用它",
	     confirmButtonColor:"ec6c62",
	   },function(){
	     $.ajax({
                    type: 'POST',
                    url: '/Admin/SysUserManager/',
                    data: {
                        'objectId': id,
                        'forbidden':state, 
                        'csrfmiddlewaretoken': $('#csrfProductManager input[name="csrfmiddlewaretoken"]').prop('value')
                    },
                    success: function (data) {
		      swal('禁用成功');

			 if(forbid.hasClass('forbid')){
			   forbid.removeClass('forbid').addClass('restore');
			   forbid.text('恢复');
			   console.log(forbid.prev());
			   forbid.prev()[0].innerText = '禁用';
			 }else{
			   forbid.removeClass('restore').addClass('forbid');
			   forbid.text('禁用');
			   console.log(forbid.prev());
			   forbid.prev()[0].innerText = '正常';
			 }

                    },
                   error: function(XMLHttpRequest, textStatus, errorThrown) {
                      swal("禁用失败");

                   },
               });
	   }
	 );
         }else{
	 swal(
	   {
	     title:"你确定恢复它吗？",
	     text:"恢复之后此账号可以正常使用",
	     type:"warning",
	     showCancelButton:true,
	     closeOnConfirm:false,
	     confirmButtonText:"是的，我要恢复它",
	     confirmButtonColor:"ec6c62",
	   },function(){
	     $.ajax({
                    type: 'POST',
                    url: '/Admin/SysUserManager/',
                    data: {
                        'objectId': id,
                        'forbidden':state, 
                        'csrfmiddlewaretoken': $('#csrfProductManager input[name="csrfmiddlewaretoken"]').prop('value')
                    },
                    success: function (data) {
		      swal('恢复成功');

			 if(forbid.hasClass('forbid')){
			   forbid.removeClass('forbid').addClass('restore');
			   forbid.text('恢复');
			 }else{
			   forbid.removeClass('restore').addClass('forbid');
			   forbid.text('禁用');
			 }

                    },
                   error: function(XMLHttpRequest, textStatus, errorThrown) {
                      swal("恢复失败");

                   },
               });
	   }
	 );
        }

       },
       deleteUser(e,id){
         let target = $(e.currentTarget).parent();
	 swal(
	   {
	     title:"你确定删除它吗？",
	     text:"删除之后此账号将消失",
	     type:"warning",
	     showCancelButton:true,
	     closeOnConfirm:false,
	     confirmButtonText:"是的，我要删除它",
	     confirmButtonColor:"ec6c62",
	   },function(){
	     $.ajax({
                    type: 'POST',
                    url: '/Admin/SysUserManager/',
                    data: {
                        'objectId':id,
                        'state': 1,
                        'csrfmiddlewaretoken': $('#csrfProductManager input[name="csrfmiddlewaretoken"]').prop('value')
                    },
                    success: function (data) {
		      swal("删除成功");
		      target.empty();
		      
                    },
                   error: function(XMLHttpRequest, textStatus, errorThrown) {
		     swal("删除失败");
                   },
               });
	   }
       );

      },
  }

 }
</script>

<style>

</style>
