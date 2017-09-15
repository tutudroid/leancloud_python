<template>
	<div class="activityManaVue">
		<div class="shown">
			<h2>活动管理</h2>
			<hr>
			<div class="activities" v-for="activity in activitymodels.on">
				<div><input type="checkbox" v-model="activities" checked><label>activity.name</label><span class="link" @click="config($event,activity.name)">配置</span></div>
			</div>
			<div class="activities" v-for="activity in activitymodels.off">
				<div><input type="checkbox" v-model="activities"><label>activity.name</label><span class="link" @click="config(activity.name)">配置</span></div>
			</div>
		</div>
		<div class="freightFree config hide">
			<h2>满X元包邮活动配置</h2>
			<hr>
			<span class="link" @click="toggle()">返回</span>
			<div class="condition">
				<span>优惠条件:</span><div>订单总价满:<input type="text" name="lowestConditinPrice">元免运费</div>
			</div>
			<div class="excludeDistrict">
				<h3>不参加活动的地区</h3>
				<div class="content">
					<div class="firstCol" v-for="add in addressProvince">
						<input type="checkbox" @click="toggleCheck($event)"><label>add.name</label>
						<div class="secondCol" v-for="addCity in addressProvince.AddressCity">
							<input class="excludeCities" type="checkbox" v-if="excludeCities.find(function(item){item == addCity}) != undefined" checked :name="addCity.name">
							<input class="excludeCities" type="checkbox" v-else :name="addCity.name"><label>addCity.name</label>
						</div>
					</div>
					<span class="link" @click="saveFreight()">保存</span>
				</div>
			</div>
		</div>
	</div>	
</template>
<script>
	export default{
		data:function(){
			return {
				activities:[],
				excludeCities:[],
				addressProvince:[],
			}
		},
		props:["activitymodels"],
		methods:{
			toggle(hideName="hide"){
				let shown = $('.shown');
				let hide = $(hideName);
				if(shown.hasClass('shown')){
					shown.removeClass('shown').addClass('hide');
				}
				if(hide.hasClass('hide')){
					hide.removeClass('hide').addClass('shown');
				}
			},
			config(e,name){
				let checked = $(e.currentTarget).prev().prev().attr('checked');
				let ok1 = 0;
				let ok2 = 0;
				if(name == "满X元包邮活动配置" && checked){
					$.ajax({
			          type: 'GET',
			          url: '/xx/xx/',
			          data: {
			             
			          },
			          success: function (data) {
			            let dataJson = JSON.parse(data);
			            _this.addressProvince = dataJson.xx;
			            ok1 = 1;
			            
			          },
			          error: function(XMLHttpRequest, textStatus, errorThrown) {
			           swal('抓取不到数据')
			          },
			      	});
			      	$.ajax({
			          type: 'GET',
			          url: '/xx/xx/',
			          data: {
			             
			          },
			          success: function (data) {
			            let dataJson = JSON.parse(data);
			            _this.excludeCities = dataJson.xx;
			            ok2 = 1;
			            
			          },
			          error: function(XMLHttpRequest, textStatus, errorThrown) {
			           swal('抓取不到数据')
			          },
			      	});
			      	swal({
				        title: "加载地址数据中",
				        text:"你这么可爱，就等待一下呗",
				        timer: 2000,
				        showConfirmButton: false
			      	});
			      	if(ok1==1 && ok2==1){
			      		toggle(".freightFree");
			      	}
				}
			},
			toggleCheck(e){
				let province = $(e.currentTarget);
				let city = $(e.currentTarget).children('.secondCol').children('input');
				if(province.attr('checked')){
					for(let prop in foo){
						if(prop > -1){
							foo[prop].attr("checked","checked");
						}
					}
				}else{
					for(let prop in foo){
						if(prop > -1){
							foo[prop].attr("checked","");
						}
					}
				}
			},
			saveFreight(){
				let excludeCities = $('.excludeCities[checked="checked"]');
				let nameElements = [];
				let names = [];
				let lowestConditinPrice = $('.lowestConditinPrice').val();
				for(prop in excludeCities){
					if(prop > -1){
						nameElements.push(excludeCities[prop]);
					}
				}
				names = nameElements.map(function(item){
					return $(item).attr('name');
				});
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
		            type: 'xx',
		            url: '/xx/xx/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {
		            	names:names,	
		            	sum:lowestConditinPrice,	            	
		            },
		            success: function (data) {
		              swal("满X元包邮已经修改");
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("满X元包邮修改失败");
		            },           
		          });
        		});
			}
		}
	}
</script>
