<template>
  <div class="searchAppUserVue">
    <div class=container>
      <div class="row gap">
        <form class="form-inline">
          <div class="form-group">
            <label for="userId">用户Id</label>
            <input type="text" class="form-control" id="userId" v-model="userId">
          </div>
          <div class="form-group">
            <label for="userName">用户名</label>
            <input type="text" class="form-control" id="userName" v-model="userName">
          </div>
          <div class="form-group">
            <label for="userPhoneNum">手机号</label>
            <input type="text" class="form-control" id="userPhoneNum" v-model="userPhoneNum">
          </div>
       </form>    	

      </div>
      
      <div class="row gap">
        <form class="form-inline">
          <div class="form-group">
            <label for="nickName">昵称</label>
            <input type="text" class="form-control" id="nickName" v-model="nickName">
          </div>
          <div class="form-group">
            <label for="registerDate">注册时间</label>
            <input type="date" class="form-control" id="registerDate" v-model="registerDate">
          </div>
          <div class="form-group">
            <label for="registerDateEnd">至</label>
            <input type="date" class="form-control" id="registerDateEnd" v-model="registerDateEnd">
          </div>
       </form>    	

      </div>
    </div>

    <div class="gap">
      <span class="longButton" @click="search()">搜索</span>
    </div>

    <hr>

    <div class="gap">
    
      <table class="table table-striped">
        <thead>
          <tr>
            <th>用户名</th>
	    <th>手机号</th>
	    <th>昵称</th>
	  </tr>
	</thead>

	<tbody>
          <tr class="searchResult">
            <td>ASHA</td>
	    <td>18816500304</td>
	    <td>asha</td>
	  </tr>
          <tr class="searchResult">
            <td>PETER</td>
	    <td>16723662367</td>
	    <td>peter</td>
	  </tr>
	</tbody>
      </table>

    </div>
    

  </div>
</template>

<script>
  export default {
      data:function(){
        return {
	  userId:"",
	  userName:"",
          userPhoneNum:"",
	  nickName:"",
	  registerDate:"",
	  registerDateEnd:""
	}
      },
      methods:{
        search(){
	  alert("用户id:"+this.userId+" 用户姓名"+this.userName+" 手机号:"+this.userPhoneNum+" 昵称:"+this.nickName+" 注册时间:"+this.registerDate+" 至时间:"+this.registerDateEnd);
	}
      }
  }
</script>



<style>

.longButton{
  border: 2px solid;
  padding: 8px 100px;
  background-color: cyan;
  cursor:pointer;
}
  
</style>
