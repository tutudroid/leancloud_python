<template>
	<div class="ServiceListVue">
		<div class="content shown">
			<h2>基础服务列表</h2>
			<hr>
			<span class="link" @click="toggle('.addService')">添加服务</span>
			<table class="table table-bordered">
				<thead>
				  <th>服务名</th>
				  <th>服务详情</th>
				  <th>编辑</th>
				  <th>删除</th>
				</thead>
				<tbody>
					<tr v-for="s in servicelist"> 
						<td>{{s.name}}</td>
						<td>{{s.breifDescription}}</td>
						<td class="link" @click="toggle('.edit',s.objectId,s.name,s.breifDescription)">编辑</td>
						<td class="link" @click="deleteService($event,s.objectId)">删除</td>
					</tr>
				</tbody>
			</table>
		</div>
		<div class="addService hide">
			<h2>添加商品服务</h2>
			<hr>
			<span class="link" @click="toggle()">返回</span>
			<div class="control-group">
				<label class="control-label" for="name">服务名称</label>
				<div class="controls">
					<input class="medium" type="text" id="name" v-model="name">
				</div>
			</div>
			<div class="control-group">
				<label class="control-label" for="breifDescription">服务简介</label>
				<div class="controls">
					<textarea cols="10" rows="20" v-model="breifDescription"></textarea>
				</div>
			</div>
			<span class="link" @click="addService()">确认</span>
		</div>
		<div class="edit hide">
			<h2>编辑商品服务</h2>
			<hr>
			<span class="link" @click="toggle()">返回</span>
			<div class="control-group">
				<label class="control-label" for="name">服务名称</label>
				<div class="controls">
					<input class="medium" type="text" id="name" v-model="name" :value="name">
				</div>
			</div>
			<div class="control-group">
				<label class="control-label" for="breifDescription">服务简介</label>
				<div class="controls">
					<textarea cols="10" rows="20" v-model="breifDescription">{{breifDescription}}</textarea>
				</div>
			</div>
			<span class="link" @click="editService()">确认</span>
		</div>
	</div>
</template>
<script>
	export default{
		data:function(){
			return {
				objectId:"",
				name:"",
				breifDescription:"",
			}
		},
		props:["servicelist"],
		methods:{
			toggle(hide1=".hide",id,name,desc){
				if(hide == ".edit"){
					this.objectId = id;
					this.name = name;
					this.breifDescription = desc;
				}else{					
					this.name = "";
					this.breifDescription = "";
				}
				let shown = $('.shown');
				let hide = $(hide1);
				if(shown.hasClass('shown')){
					shown.removeClass('shown').addClass('hide');
				}
				if(hide.hasClass('hide')){
					hide.removeClass('hide').addClass('shown');
				}
			},
			deleteService(e,id){
				let remove = $(e.currentTarget).parent();
				swal({
		          title: "你确定删除这一个服务吗?",
		          text: "",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我要删除它!",
		          closeOnConfirm: false
		        },
		        function(){
		          $.ajax({
		            type: 'xx',
		            url: '/xx/xx/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {
		            	objectId:id,
		            },
		            success: function (data) {
		              swal("此商品被成功删除");
		              $(remove).remove();
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("此商品删除失败");
		            },           
		          });
		        });
			},
			editService(){
				swal({
		          title: "你确定更新这一个服务吗?",
		          text: "",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我要更新它!",
		          closeOnConfirm: false
		        },
		        function(){
		          $.ajax({
		            type: 'xx',
		            url: '/xx/xx/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {
		            	objectId:id,
		            },
		            success: function (data) {
		              swal("此服务被成功更新");
		              $(remove).remove();
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("此服务更新失败");
		            },           
		          });
		        });
			},
			addService(){
				swal({
		          title: "你确定新增这一个服务吗?",
		          text: "",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我要新增它!",
		          closeOnConfirm: false
		        },
		        function(){
		          $.ajax({
		            type: 'xx',
		            url: '/xx/xx/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {
		            	name:_this.name,
						breifDescription:_this.breifDescription,
		            },
		            success: function (data) {
		              swal("此商品成功增加");
		              $(remove).remove();
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("此商品新增失败");
		            },           
		          });
		        });
			},
		},
	}
</script>


