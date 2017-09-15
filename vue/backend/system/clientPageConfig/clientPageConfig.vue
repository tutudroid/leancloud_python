<template>
   <div class="clientPageConfigVue">
    <div class="one shown">
        <div class="gap">
          <span class="mySpan" @click="editConfig()">编辑</span>
	</div>
	<table class="table table-striped" v-if="configs.length>0">
	  <thead>
	    <tr>
	      <td>编码</td><td>名称</td><td>URL</td><td></td>
	    </tr>
	  </thead>

	  <tbody>
	    <tr class="clientPageConfig" v-for="config in configs">
              <td>{{config.code}}</td><td>{{config.name}}</td><td>{{config.url}}</td>     	      
	    </tr>
	  </tbody>

	</table>
    </div>

    <div class="changeOnConfig hide">

    <div class="gap">
      <span class="mySpan" @click="addConfig()">添加</span>
	</div>
    
	<table class="table table-striped">
	  <thead>
	    <tr>
	      <td>编码</td><td>名称</td><td>URL</td>
	    </tr>
	  </thead>

	  <tbody>
	    <tr class="clientPageConfigResult" v-for="config in configs">
              <td><input type="text" :value="config.code"></td><td><input type="text" :value="config.name"></td><td><input type="text" :value="config.url"></td><td class="link" @click="deleteConfig(index)">删除</td>     	      
	    </tr>
	  </tbody>

	</table>

	<div>
          <span class="mySpan" @click="saveConfig()">保存</span>
          <span class="mySpan" @click="toggleShow()">取消</span>
	</div>
	      
    </div>

  </div>
</template>

<script>
  import {linkedList} from '../../../lib/linkedList.js'
  export default{
    data:function(){
      return{
        
      }
    },
    props:['configs'],
    methods:{
      editConfig(){
        this.toggleShow();
      },
      toggleShow(){
        let shown = $(".clientPageConfig .shown");
		let hide = $(".clientPageConfig .hide");
        if(shown.hasClass('shown')){
	  		shown.removeClass('shown').addClass('hide');
	    }
		if(hide.hasClass('hide')){
		    hide.removeClass('hide').addClass('shown');
		}
      },
      saveConfig(){
        let configs = $('.clientPageConfigResult');
		let hasEmpty = false;
		let configsDetails = [];
		let allConfigs = [];
		configs.each(
		  function(index){
		    configsDetails[index]=$(this).children();
		  }
		);
		$(configsDetails).each(
		  function(inputIndex){		      
		      let inputs = $(this).children();
		      let parConfig = [];
		      $(inputs).each(
		        function(tdIndex){			  
				  if($(this).val() == ""){
				    hasEmpty = true;			    
				  }
			  	  parConfig[tdIndex] = $(this).val();
			    }
		      );		   
	          allConfigs[inputIndex] = parConfig;
		  }
		);
		if(hasEmpty){
		   swal("Oops...","新添加中的编辑存在空值，请添加或删除","error");
		   allConfigs = [];
		}else{
			
			let filterConfigs = allConfigs.filter(
				function(configs){
				  return configs.length != 0;
				}
			);
			let WebPageConfigure = filterConfigs.map(
			    function(config){
			      var obj = {};
			      obj['code'] = config[0];
			      obj['name'] = config[1];
			      obj['url'] = config[2];			    
			      return obj;
			    }
			);
			let w = {};
			w['WebPageConfigure'] = WebPageConfigure;
			swal(
				{
					title:"确定保存吗？",
					text:"此操作将影响客户端的配置内容",
					type:"warning",
					showCancelButton:true,
					closeOnConfirm: false,
					confirmButtonText: "我要保存",
					confirmButtonColor: "#b5d5ff",
				},function(){
					$.ajax({
	                    type: 'POST',
	                    url: '/Admin/WebPageConfigure/',
	                    headers: {
                             'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
                        },
	                    contentType: "application/json; charset=utf-8",
                        dataType: "json",
	                    data: JSON.stringify(w),
	                    success: function (data) {
	                       swal("配置成功");
	                    },
	                   error: function(XMLHttpRequest, textStatus, errorThrown) {
	                       swal("保存配置失败");
	                    },
	                    
                	});
						
				}
			);
	    }
      },
      addConfig(){
		let added = '<tr class="clientPageConfigResult"><td><input type="text"></td><td><input type="text"></td><td><input type="text"><td class="link abandon">放弃</td></tr>';
		$(added).appendTo('.changeOnConfig tbody');
        $('.abandon').bind('click',function(e){
          let newConfig = $(e.target.parentElement);
	  	  newConfig.empty();
        })
      },
      deleteConfig(id){        
		swal(
		  {
		    title:"你确定吗？",
		    text:"你真的要删除这个配置吗？",
		    type:"warning",
		    showCancelButton:true,
		    closeOnConfirm:false,
		    confirmButtonText:"是的，我要删除",
		    confirmButtonColor:"ec6c62"
		  },function(){
			axios.post('https://unpkg.com/axios/dist/axios.min.js', {
			    
			  })
			  .then(function (response) {
			    swal("文件成功删除");
			  })
			  .catch(function (error) {
			    swal("删除失败");
			  });
		  }
		);
      },
     
    }
}
</script>


