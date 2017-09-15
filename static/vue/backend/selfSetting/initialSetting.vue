<template>
	<div class="initialSettingVue">

		  <div class="form-group">
		    <label for="selfShopName">自营店名</label>
		    <input type="text" class="form-control" id="selfShopName" v-model="selfShopName">
		  </div>
		  <div class="form-group">
		    <label for="managerPhone">管理人手机号</label>
		    <input type="text" class="form-control" id="managerPhone" v-model="managerPhone">
		  </div>
		  <div class="form-group">
		    <label for="brandName">品牌名</label>
		    <input type="text" class="form-control" id="brandName" v-model="brandName">
		  </div>
		  <div class="form-group">
		    <label for="file1">添加品牌Logo</label>
		    <input class="file" id="file1" type='file' style="display:none;">
   			<div id="prev_file1">
   				<div class="prev_thumb" style="background-image:url('default.jpg');"></div>
   			</div><br/>
		  </div>
		  <div class="form-group">
		    <label for="brandDesc">品牌简介</label>
		    <input type="text" class="form-control" id="brandDesc" v-model="brandDesc">
		  </div>
		  <span class="btn btn-default" @click="initialSelfShop()">提交</span>

	</div>	
</template>
<script>
	$(document).ready(function()
	{
	    $('.file').preimage();
	});
	export default{
		data:function(){
			return {
				selfShopName:"",
				managerPhone:"",
				brandName:"",
				brandDesc:"",
			}
		},
		methods:{
			initialSelfShop(){
				let _this = this;
				let brandLogo = $('.initialSettingVue .prev_thumb').attr('style').slice(23);
				swal({
		          title: "你确定信息都正确了吗?",
		          text: "若不确定请仔细检查一下哦",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我确认信息无误!",
		          closeOnConfirm: false
		        },
		        function(){
		          $.ajax({
		            type: 'post',
		            url: '/Shop/InitiateDirectShop/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {
		            	selfShopName:this.selfShopName,
						managerPhone:this.managerPhone,
						brandName:this.brandName,
						brandDesc:this.brandDesc,
						brandLogo:brandLogo,
		            },
		            success: function (data) {
		              swal("自营商店已经初始化成功");
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("自营商店初始化失败");
		            },           
		          });
        		});
			},
		},
	}
</script>
<style type="text/css">
	
.prev_container{
	overflow: auto;
	width: 300px;
	height: 135px;
}

.prev_thumb{
	margin: 10px;
	height: 100px;
	width: 100px;
}

</style>