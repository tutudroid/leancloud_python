<template>
	<div class="selfShopManaVue">
		<div class="info shown">
			<h2>自营店信息</h2>
			<hr>
			<span class="link" @click="toggle()">编辑</span>
			<h3>自营店店名:</h3>
			<div class="content">{{selfshop.name}}</div>
			<h3>管理员手机号</h3>
			<div class="content">{{selfshop.phone}}</div>
		</div>

		<div class="edit hide">
			<h2>修改自营店信息</h2>
			<hr>
			<span class="link" @click="toggle()">返回</span>
			<label for="selfShopName">自营店名</label>
			<input type="text" v-model="selfShopName" id="selfShopName" class="contentInput" :value="selfshop.name">
			<label for="managerPhone">管理员手机号</label>
			<input type="text" v-model="managerPhone" id="managerPhone" class="contentInput" :value="selfshop.phone">
			<span class="save link" @click="save()">保存</span>
		</div>
	</div>
</template>
<script>
	export default{
		data:function(){
			return {
				selfShopName:"",
				managerPhone:"",
			}
		},
		props:["selfshop","selfshopid"],
		methods:{
			toggle(){
				let shown = $('.shown');
				let hide = $('.hide');
				if(shown.hasClass('shown')){
					shown.removeClass('shown').addClass('hide');
				}
				if(hide.hasClass('hide')){
					hide.removeClass('hide').addClass('shown');
				}
			},
			save(){
				let _this = this;
				swal({
		          title: "确定修改自营商铺信息吗?",
		          text: "",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我确认!",
		          closeOnConfirm: false
		        },
		        function(){
		          $.ajax({
		            type: 'get',
		            url: '/Shop/EditDirectShop/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {
		            	objectId:_this.selfshopid,
					    shopName: _this.selfShopName,
					    phoneNumber: _this.managerPhone,
		            },
		            success: function (data) {
		              swal("信息已经修改");
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("信息修改失败");
		            },           
		          });
        		});
			}
		}
	}
</script>