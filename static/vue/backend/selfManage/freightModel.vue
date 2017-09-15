freightmodels
<template>
	<div class="freightModelsVue">
		<div class="one shown">
			<h2>运费模版</h2>
			<hr>
			<span class="link" @click="toggleAddNew()">新增运费模版</span>
			<div v-for="model in freightmodels">
				<span class="content">model.name</span>\
				<span class="content" v-if="model.isFreightFree">包邮</span><span class="content" v-else>model.freight</span>
				<span class="content link" @click="reviseModel(model.name,model.isFreightFree,model.freight)">修改</span><span class="delemeter">/</span><span class="content link" @click="deleteModel($event,model.objectId)">删除</span>
			</div>
		</div>
		<div class="revise hide">
			<h2>编辑运费模版</h2>
			<hr>
			<span class="link" @click="toggle()">返回</span>
			<label for="modelName">模版名称</label>
			<input id="modelName" type="text" v-model="modelName"></input>
			<input type="radio" v-model="modelFee" v-if="isFreightFree" checked="" :value="true" name="modelFee" ><input type="radio" v-model="modelFee" v-else name="modelFee" :value="true"><label>包邮</label>
			<input type="radio" v-model="modelFee" v-if="!isFreightFree" checked="" name="modelFee" :value="false"><input type="radio" v-model="modelFee" v-else name="modelFee" :value="false"><input type="text" v-model="fee" v-if="!isFreightFree" :value="freight"><input type="text" v-model="fee" v-else ><label>设置运费</label>
			<span @click="saveRevise()">保存</span>
		</div>		
		<div class="addNew hide">
			<h2>新增运费模版</h2>
			<hr>
			<span class="link" @click="toggle()">返回</span>
			<label for="modelName">模版名称</label>
			<input id="modelName" type="text" v-model="modelName"></input>
			<input type="radio" v-model="modelFee" name="modelFee" :value="true"><label>包邮</label>
			<input type="radio" v-model="modelFee" name="modelFee" :value="false"><label>设置运费</label><input type="text" v-model="fee">元
			<span class="link" @click="saveAddNew()" >保存</span>
		</div>
	</div>
</template>
<script>
	export default{
		data:function(){
			return {
				modelName:"",
				modelFee:"",
				fee:"",
			}
		},
		props:["freightmodels"],
		methods:{
			toggle(){
				let hide = $('.freightModelsVue').children('.one');
				let hideAddNew = $('.addNew');
				let hideRevise = $('.revise');
				if(hideAddNew.hasClass('shown')){
					hideAddNew.removeClass('shown').addClass('hide');
					hide.removeClass('hide').addClass('shown');
				}
				if(hideRevise.hasClass('shown')){
					hideRevise.removeClass('shown').addClass('hide');
					hide.removeClass('hide').addClass('shown');
				}
			},
			toggleAddNew(){
				this.modelFee = "";
				this.modelName = "";
				this.fee = "";
				let shown = $('.shown');
				let hideAddNew = $('.addNew');
				if(shown.hasClass('shown')){
					shown.removeClass('shown').addClass('hide');
				}
				if(hideAddNew.hasClass('hide')){
					hideAddNew.removeClass('hide').addClass('shown');
				}
				
			},
			toggleRevise(){
				let shown = $('.shown');
				let hideRevise = $('.revise');
				if(shown.hasClass('shown')){
					shown.removeClass('shown').addClass('hide');
				}
				if(hideRevise.hasClass('hide')){
					hideRevise.removeClass('hide').addClass('shown');
				}

			},
			reviseModel(name,isFreightFree,freight){
				this.modelName = name;
				this.modelFee = isFreightFree;
				this.fee = freight;
				this.toggleRevise();
			},
			saveRevise(){
				let _this = this;
				swal({
		          title: "你确定修改吗?",
		          text: "",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我确定!",
		          closeOnConfirm: false
		        },
		        function(){
		          $.ajax({
		            type: 'get',
		            url: '/Shop/EditFreightModel/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {
		            	modelName:_this.modelName,
		            	modelFee:_this.modelFee,
		            	fee:_this.fee,		
		            },
		            success: function (data) {
		              swal("运费模版已经修改");
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("运费模版修改失败");
		            },           
		          });
        		});
			},
			saveAddNew(){
				let _this = this;
				swal({
		          title: "你确定新增吗?",
		          text: "",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我确定!",
		          closeOnConfirm: false
		        },
		        function(){
		          $.ajax({
		            type: 'get',
		            url: '/Shop/EditFreightModel/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {
		            	modelName:_this.modelName,
		            	modelFee:_this.modelFee,
		            	fee:_this.fee,		
		            },
		            success: function (data) {
		              swal("运费模版已经新增");
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("运费模版新增失败");
		            },           
		          });
        		});
			},
			deleteModel(e,id){
				let _this = this;
				let record = $(e.currentTarget).parent();
				swal({
		          title: "你确定删除这个运费模版吗?",
		          text: "删除模版之后将无法恢复",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我确定删除!",
		          closeOnConfirm: false
		        },
		        function(){
		          $.ajax({
		            type: 'get',
		            url: '/Shop/DeleteFreightModel/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {
		            	objectId:id,		           
		            },
		            success: function (data) {
		              swal("运费模版已经成功删除");
		              $(record).remove();
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("运费模版删除失败");
		            },           
		          });
        		});
			}

		}
	}
</script>