<template>

<div class="container">
<form class="form-horizontal" action="" method="post">
  <div class="form-group">
    <label for="account" class="col-sm-2 control-label">账号</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="account">
    </div>
  </div>
  <div class="form-group">
    <label for="password" class="col-sm-2 control-label">密码</label>
    <div class="col-sm-10">
      <input type="password" class="form-control" id="password">
    </div>
  </div>
  <button class="btn btn-default">登入</button>
</form>
</div>

</template>

<style>

  .container{
    text-align:center;
  }
  form{
    position: relative;
    top: 200px;
    width: 40%;
    display: inline-block;
  }
</style>
