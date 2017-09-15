brandlists
<template>
	<div class="selfBrandListVue">
		<div class="shown">
			<span class="link" @click="toggleAdd('.add')">添加品牌</span>
			<table class="table table-striped">
				<thead>
					<th>品牌名</th><th>品牌Logo</th><th>简介</th><th>编辑</th>
				</thead>
				<tbody>
					<tr v-for="brand in brandlists"><td>brand.name</td><td><img src="brand.imageFile"></td><td>brand.breifDescription</td><td @click="revise('.revise',brand.objectId,brand.name,brand.imageFile,brand.breifDescription)">修改</td></tr>
				</tbody>
			</table>
		</div>
		<div class="add hide">
			  <h2>添加品牌</h2>
			  <hr>
			  <span class="link" @click="toggle('.add')">返回</span>
			  <div class="form-group">
			    <label for="brandName">品牌名称</label>
			    <input type="text" class="form-control" id="brandName" v-model="brandName">
			  </div>
			  <div class="form-group">
			    <label for="file1">添加品牌Logo</label>
			    <input class="file" id="file1" type='file'/ style="display:none;">
	   			<div id="prev_file1">
	   				<div class="prev_thumb" style="background-image:url('default.jpg');"></div>
	   			</div><br/>
			  </div>
			  <div class="form-group">
			    <label for="brandDesc">品牌简介</label>
			    <input type="text" class="form-control" id="brandDesc" v-model="brandDesc">
			  </div>
			  <span class="btn btn-default" @click="addBrand()">确定</span>
		</div>
		<div class="revise hide">
			  <h2>修改品牌信息</h2>
			  <hr>
			  <span class="link" @click="toggle('.revise')">返回</span>
			  <div class="form-group">
			    <label for="brandName">品牌名称</label>
			    <input type="text" class="form-control" id="brandName" v-model="brandName" >
			  </div>
			  <div class="form-group">
			    <label for="file1">添加品牌Logo</label>
			    <input class="file" id="file1" type='file'/ style="display:none;">
	   			<div id="prev_file1">
	   				<div class="prev_thumb" :style="'background-image:url('+imageFile+');'"></div>
	   			</div><br/>
			  </div>
			  <div class="form-group">
			    <label for="brandDesc">品牌简介</label>
			    <input type="text" class="form-control" id="brandDesc" v-model="brandDesc">
			  </div>
			  <span class="btn btn-default" @click="addBrand()">确定</span>
		</div>
	</div>	
</template>
<script>
	export default{
		data:function(){
			return {
				brandName:"",
				brandDesc:"",
				objectId:"",
				imageFile:"",
			}
		},
		methods:{
			toggle(hideName="hide",id="",name="",imageFile="",desc=""){
				if(hideName = ".add"){
					this.brandDesc="";
					this.brandName="";
				}else{
					this.brandName = name;
					this.brandDesc = desc;
					this.objectId = id;
					this.imageFile = imageFile;
				}
				let shown = $('.shown');
				let hide = $(hideName);
				if(shown.hasClass('shown')){
					shown.removeClass('shown').addClass('hide');
				}
				if(hide.hasClass('hide')){
					hide.removeClass('hide').addClass('shown');
				}
			},
			addBrand(){
				let _this = this;
				let image = $('.add prev_thumb').attr("src").slice(23);
				swal({
		          title: "你确定新增吗?",
		          text: "",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我要增加!",
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
		            	brandDesc:_this.brandDesc,
		            	brandName:_this.brandName,
		            	imageFile:image,
		            },
		            success: function (data) {
		              swal("自营品牌新增成功");
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("自营品牌新增失败");
		            },           
		          });
        		});
			},
			revise(){
				let _this = this;
				let image = $('.revise prev_thumb').attr("src").slice(23);
				if(_this.brandDesc=="" || _this.brandName=="" || _this.objectId=="" || image==null){
					swal("存在空值");
				}else{
					swal({
			          title: "你确定修改吗?",
			          text: "",
			          type: "warning",
			          showCancelButton: true,
			          confirmButtonColor: "#DD6B55",
			          confirmButtonText: "是的,我要修改!",
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
			            	brandDesc:_this.brandDesc,
			            	brandName:_this.brandName,
			            	objectId:_this.objectId,
			            	imageFile:image,
			            },
			            success: function (data) {
			              swal("自营品牌修改成功");
			            },
			            error: function(XMLHttpRequest, textStatus, errorThrown) {
			              swal("自营品牌修改失败");
			            },           
			          });
	        		});
	        	}
			}
		}
	}
</script>