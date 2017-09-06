<template>
 <div class="forgetPwdFormVue">
  <div>返回</div>
  <div class="form-group">
    <label for="account" class="col-sm-2 control-label">萌趣账号</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="account" v-model="username">
    </div>
  </div>
  <div class="nextStep">下一步</div>
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
    <label for="password" class="col-sm-2 control-label">新密码</label>
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
  <span class="btn btn-default" @click="confirm()">确认</span>
 </div>
</template>
