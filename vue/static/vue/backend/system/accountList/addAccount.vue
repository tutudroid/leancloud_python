<template>

<div id="addAccountVue">
  
  <div class="control-group">
    <label class="control-label" for="userName">用户名</label>
    <div class="controls">
      <input class="medium" type="text" id="userName" v-model="userName" name="username">
    </div>
  </div>
  <div class="control-group">
    <label class="control-label" for="password">密码</label>
    <div class="controls">
      <input class="medium" type="password" id="password" v-model="pwd">
    </div>
  </div>
  <div class="control-group">
    <label class="control-label" for="confirmPassword">密码</label>
    <div class="controls">
      <input class="medium" type="password" id="confirmPassword" v-model="confirmPwd">
    </div>
  </div>
  <div class="control-group">
    <label class="control-label" for="role">角色选择</label>
    <div class="controls">
      <select class="small" v-model="role">
        <option value="Shop">商家</option>
        <option value="ProductAdmin">商品管理员</option>
        <option value="CustomService">客服</option>
        <option value="BusinessOperation">运营</option>
      </select>
    </div>
  </div>
  <div class="control-group">
    <div class="controls">	
      <span class="btn myBtn" @click="register">注册</span>
    </div>
  </div>

</div>

</template>

<script>

export default {
    data: function(){
      return {
        userName:"",
	pwd:"",
	confirmPwd:"",
	role:'',
      }
    },
    methods:{
      register(){
         let csrf = $('#csrfAddSysUser input[name=csrfmiddlewaretoken]').val();
	 
         
                 $.ajax({
                    type: 'POST',
                    url: '/Admin/AddUser/',
                    data: {
                        'username': this.userName,
                        'password': this.pwd,
			'passwordSure':this.confirmPwd,
			'role':this.role,
                        'csrfmiddlewaretoken': csrf
                    },
                    success: function (data) {

                       swal("新增成功");
                    
                    },
                    error: function(XMLHttpRequest, textStatus, errorThrown) {
                       swal("新增失败");
                    },
                });
	 
      }

    } 
}

</script>

