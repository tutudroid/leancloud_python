<template>
	<div class="orderSearchVue">
		<div class="searchBox">
			<label>订单号：</label><input type="text" v-model="uniqueId">
			<label>商家账号：</label><input type="text" v-model="shop">
			<label>买家账号：</label><input type="text" v-model="user">
			<label>商品编号：</label><input type="text" v-model="orderProduct">
			<label>创建时间：</label><input type="date" v-model="start">至<input type="date" v-model="end">
			<label>订单状态：</label><input type="text" v-model="state">
			<span class="btn btn-primary ">搜索</span>
		</div>
		<div class="results">

			<div class="shown">
				<div class="title">
					<span class="th">商品</span>
					<span class="th">单价</span>
					<span class="th">数量</span>
					<span class="th">买家</span>
					<span class="th">交易状态</span>
					<span class="th">总价</span>
					<span class="th">操作</span>
				</div>
				<div class="content container result" v-for="o in selforderall">
					<div class="row head">
						<div class="col-md-3">订单号:{{o.uniqueId}}</div>		
						<div class="col-md-3">下单时间:{{o.created_at}}</div>		
					</div>
					<div class="row data" v-for="m in selforderall.orderProduct">
						<div class="col-md-2">{{m.productMainImage}}</div>		
						<div class="col-md-2">{{m.productPrice}}</div>
						<div class="col-md-2">{{m.productCount}}</div>		
						<div class="col-md-2">{{o.user.name}}</div>
						<div class="col-md-1">{{m.orderState}}</div>		
						<div class="col-md-1">{{m.productPrice*m.productCount}}</div>
						<div class="col-md-1 link" @click="toggle('detail',o.uniqueId,o.logisticsInfo,o.productComment,m.user,o.receiverName,o.receiverPhoneNumber,o.receiverAddress,o.orderProduct)">查看详情</div>		
					</div>
				</div>
			</div>
			<div class="hide">
				<h2>订单状态：{{orderState}}</h2>
				<hr>
				<div class="operate">
					<span class="sendGood myBtn" data-toggle="modal" data-target="modal1111" v-if="orderState==1">发货</span>
							<div class="modal1111 fade" tabindex="-1" role="dialog">
							    <div class="modal-dialog" role="document">
								    <div class="modal-content">
								      <div class="modal-header">
								        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
								        <h4 class="modal-title">发货</h4>
								      </div>
								      <div class="modal-body">
								      	<label>配送公司</label>
								        <select v-model="sendCompany">
								        	<option>顺风</option>
								        	<option>EMS</option>
								        </select>
								        <label>配送单号</label>
								        <input type="text" v-model="sendNumber">
								      </div>
								      <div class="modal-footer">
								        <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
								        <button type="button" class="btn btn-primary" @click="sendGood(uniqueId)">保存</button>
								      </div>
								    </div><!-- /.modal-content -->
								  </div><!-- /.modal-dialog -->
							</div><!-- /.modal -->
					<span class="sendGood myBtn" @click="checkAfterService(uniqueId)" v-if="orderState==6">查看售后记录</span>
							<div class="modal2222 fade" tabindex="-1" role="dialog">
							  <div class="modal-dialog" role="document">
							    <div class="modal-content">
							      <div class="modal-header">
							        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
							        <h2 class="modal-title">售后记录</h2>
							        <hr>
							      </div>
							      <div class="modal-body">
							        <div class="backProduct">
							        	<h3>售后记录</h3>
							        	<table>
							        		<thead>
							        			<th>商品</th><th>单价</th><th>数量</th><th>买家</th><th>售后状态</th><th>原因</th>
							        		</thead>
							        		<tbody>
							        			<tr v-for="p in AfterSaleServiceRecord.orderProduct">
							        				<td>{{p.groupName}}</td>
							        				<td>{{p.productPrice}}</td>
							        				<td>{{p.productCount}}</td>
							        				<td>{{user.name}}</td>
							        				<td>已退款</td>
							        				<td>{{AfterSaleServiceRecord.refundReasonDetail }}</td>
							        			</tr>
							        		</tbody>
							        	</table>
							        	<h4>订单号：{{uniqueId}}</h4>
							        	<h4>申请时间：{{AfterSaleServiceRecord.created_at}}</h4>
							        </div>
							        <div class="process">
							        	<h3>售后进度</h3>
							        	<div v-for="process in AfterSaleServiceRecord.afterSaleProgress">
							        		<div class="time">{{process.AcceptTime}}</div>
							        		<div class="reason">{{process.AcceptStation}}</div>
							        		<div v-if="process.recordState=='2'">
							        			<div class="receiver">
							        				{{process.shopReceiverName}}
							        			</div>
							        			<div class="phone">
							        				{{process.shopReceiverPhone}}
							        			</div>
							        			<div class="address">
							        				{{process.shopReceiverAddress}}
							        			</div>
							        		</div>
							        		<div v-if="process.recordState=='3'">
							        			<div class="logisticCompany">
							        				{{process.shipperName}}
							        			</div>
							        			<div class="logisticNum">
							        				{{process.logisticsCode}}
							        			</div>
							        		</div>
							        		<div v-if="process.recordState=='4'">
							        			<div class="amount">
							        				{{process.refundSumPrice}}
							        			</div>		      
							        		</div>
							        		<hr>
							        	</div>
							        </div>
							        <div class="applyDetail" v-if="AfterSaleServiceRecord.length>0">
							        	<h3>申请单详情</h3>
							        	<div class="order">
							        		<h4>申请时间：{{AfterSaleServiceRecord.created_at}}</h4>
							        		<h4>订单号：{{AfterSaleServiceRecord.order.uniqueId}}</h4>
							        		<h4>申请单号：{{AfterSaleServiceRecord.uniqueId}}</h4>
							        		<h4>申请人：{{AfterSaleServiceRecord.user.name}}</h4>
							        	</div>
							        	<hr>
							        	<div class="product">
							        		<h4><img :src="AfterSaleServiceRecord.orderProduct.productMainImage"></h4>
							        		<h4 class="name">{{AfterSaleServiceRecord.orderProduct.groupName}}</h4>
							        		<h4 class="material">{{AfterSaleServiceRecord.orderProduct.productStyle}}</h4>
							        		<h4 class="price">{{AfterSaleServiceRecord.orderProduct.productPrice }}</h4>
							        		<h4 class="amount">{{AfterSaleServiceRecord.refundProductCount }}</h4>
							        	</div>
							        	<div class="desc">
							        		<div class="reason">原因：{{AfterSaleServiceRecord.refundReasonDetail}}</div>
							        		<div class="desc">描述：{{AfterSaleServiceRecord.refundReasonDetail}}</div>
							        		<div class="imageList"><img v-for="i in AfterSaleServiceRecord.imageList" :src="i.imageFile"></div>
							        	</div>
							        	<div class="customer">
							        		<h4 class="contactPerson">联系人:{{AfterSaleServiceRecord.contactName}}</h4>
							        		<h4 class="phone">手机号：{{AfterSaleServiceRecord.contactPhone }}</h4>
							        	</div>
							        </div>
							      </div>
							      <div class="modal-footer">
							        <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
							      </div>
							    </div><!-- /.modal-content -->
							  </div><!-- /.modal-dialog -->
							</div><!-- /.modal -->
					<span class="sendGood myBtn" data-toggle="modal" data-target="model4444" v-if="logistic.length>0">查看物流</span>
							<div class="modal4444 fade" tabindex="-1" role="dialog">
							  <div class="modal-dialog" role="document">
							    <div class="modal-content">
							      <div class="modal-header">
							        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
							        <h4 class="modal-title">物流信息</h4>
							      </div>
							      <div class="modal-body">
							        <div class="company">物流公司：{{logistic.shipperName }}</div>
							        <div class="logiNum">运单号码：{{logistic.logisticsCode  }}</div>
							        <div class="track">物流跟踪：<p v-for="l in logistic.traces">{{l.info}}</p></div>
							      </div>
							      <div class="modal-footer">
							        <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
							      </div>
							    </div><!-- /.modal-content -->
							  </div><!-- /.modal-dialog -->
							</div><!-- /.modal -->

					<span class="sendGood myBtn" data-toggle="modal" data-target="modal5555" v-if="comments.length>0">查看评价</span>
							<div class="modal5555 fade" tabindex="-1" role="dialog">
							  <div class="modal-dialog" role="document">
							    <div class="modal-content">
							      <div class="modal-header">
							        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
							        <h4 class="modal-title">评价信息</h4>
							      </div>
							      <div class="modal-body">
							        <div class="comment">
										<div class="commentContent modal fade" v-for="comment in comments">
											<div class="media modal-dialog">
												<div class="modal-content">
													<div class="modal-body">
														<div class="media-left media-middle"> 
															<a href="#"> 
															<img alt="64x64" class="media-object" data-src="holder.js/64x64" :src="comment.userAvatar" data-holder-rendered="true" style="width: 64px; height: 64px;"> </a> 
														</div>
														<div class="media-body"> 
															<h4 class="media-heading">{{comment.created_at}}</h4> 
															<p>{{comment.content}}</p> 
															<p v-for="image in comment.imageList">
																<img src="image">
															</p> 
														</div>
													</div>
												</div>
											</div>
										</div>
									</div>
							      </div>
							      <div class="modal-footer">
							        <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
							      </div>
							    </div><!-- /.modal-content -->
							  </div><!-- /.modal-dialog -->
							</div><!-- /.modal -->
				</div>
				<div class="customerInfo">
					<h3>买家信息</h3>
					<hr>
					<div>
						<h4>用户:{{user.name}}</h4>
						<h4>收件人:{{receiverName}}</h4>
						<h4>联系电话:{{receiverPhoneNumber}}</h4>
						<h4>收件地址:{{receiverAddress}}</h4>
					</div>
				</div>
				<div class="orderInfo">
					<h3>订单信息</h3>、
					<hr>
					<div>
						<h4>订单号:{{uniqueId}}</h4>
						<h4>创建时间:{{created_at}}</h4>
					</div>
				</div>
				<div class="orderProducts container">
					<div class="title">
						<span class="th">商品</span>
						<span class="th">属性</span>
						<span class="th">单价</span>
						<span class="th">数量</span>
						<span class="th">优惠</span>
						<span class="th">总价</span>
					</div>
					<div class="row data" v-for="(m,index) in orderProduct">
						<div class="col-md-2">{{m.productMainImage}}</div>		
						<div class="col-md-2">{{m.productStyle}}</div>		
						<div class="col-md-2">{{m.productPrice}}</div>
						<div class="col-md-1">{{m.productCount}}</div>		
						<div class="col-md-1"></div>
						<div class="col-md-1 link" v-if="index == m.length-1">{{totalPrice}}</div>		
					</div>
				</div>
			</div>

		</div>

	</div>

</template>

<script>
	export default{
		data:function(){
			return {
				uniqueId:"",
				shop:"",
				user:"",
				orderProduct:"",
				start:"",
				end:"",
				state:"",
				results:[],
				////////
				orderAll:[],
				waitingmoney:[],
				ontheroad:[],
				moneyback:[],
				customerwaiting:[],
				waitingcomment:[],
				finish:[],
				cancel:[],
				allorder:[],
				//
				orderState:"",
				uniqueId:"",
				created_at:"",
				//
				user:{},
				receiverName:"",
				receiverPhoneNumber:"",
				receiverAddress:"",
				orderProduct:[],
				totalPrice:0,
				//
				AfterSaleServiceRecord:{},
				//
				logistic:[],
				//
				comments:[],
			}
		},
		props:["orderSearch"],
		methods:{
			checkAfterService(id){
				let _this = this;
				let ok = 0;
				$.ajax({
				  type: 'get',
				  url: '/AfterSale/AfterSale/',
				  data: {
				     uniqueId:id,
				  },
				  success: function (data) {
				    let dataJson = JSON.parse(data);
				    _this.AfterSaleServiceRecord = dataJson;
				    ok = 1;
				    
				  },
				 error: function(XMLHttpRequest, textStatus, errorThrown) {
				   swal('抓取不到数据')
				  },
				});
				swal({
					title: "抓取售后记录信息中",
					text:"你这么可爱，就等待一下呗",
					timer: 2000,
					showConfirmButton: false
				});
				if(ok == 1){
					
				}
			},
			sendGood(id){
				swal({
		          title: "你确定发货吗?",
		          text: "",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我要发货!",
		          closeOnConfirm: false
		        },
		        function(){
		          $.ajax({
		            type: 'post',
		            url: '/Order/DisplaceOrder/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {
		            	objectId:id, 
		            	shipperCode:"xxxxxxx", 
		            	shipperName:_this.sendCompany, 
		            	logisticsCode:_this.sendNumber
		            },
		            success: function (data) {
		              swal("发货成功");
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("发货失败");
		            },           
		          });
		        });
			},
			toggle(e,detail="",logi="",productComment="",orderState,uniqueId,created_at,user,receiverName,receiverPhoneNumber,receiverAddress,orderProduct){
				if(detail == "detail"){
					this.comments = productComment;
					this.logistic = logi;
					this.orderState = orderState;
					this.uniqueId = uniqueId;
					this.created_at = created_at;
					this.user = user;
					this.receiverName = receiverName;
					this.receiverPhoneNumber = receiverPhoneNumber;
					this.receiverAddress = receiverAddress;
					this.orderProduct = orderProduct;
					orderProduct.forEach(function(item){
						this.totalPrice += item.productPrice;
					});
				}
				let shown = $('.shown');
				let hide = $('.hide');
				if(shown.hasClass('shown')){
					shown.removeClass('shown').addClass('hide');
				}
				if(hide.hasClass('hide')){
					hide.removeClass('hide').addClass('shown');
				}
			},
		},
	}
</script>