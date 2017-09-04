<template>
   <div class="clientPageConfigVue">
    <div class="one shown">
        <div class="gap">
          <span class="mySpan" @click="editConfig()">编辑</span>
	</div>
	<table class="table table-striped">
	  <thead>
	    <tr>
	      <td>编码</td><td>名称</td><td>URL</td><td></td>
	    </tr>
	  </thead>

	  <tbody>
	    <tr class="clientPageConfig">
              <td>1</td><td>隐私政策</td><td>mengqu.leanapp.cn/....</td>     	      
	    </tr>
	    <tr class="clientPageConfig">
              <td>2</td><td>用户协议</td><td>mengqu.leanapp.cn/....</td>      	      
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
	    <tr class="clientPageConfigResult">
              <td><input type="text" v-model="code[0]"></td><td><input type="text" v-model="name[0]"></td><td><input type="text" v-model="url[0]"></td><td class="link" @click="deleteConfig(1)">删除</td>     	      
	    </tr>
	    <tr class="clientPageConfigResult">
              <td><input type="text" v-model="code[1]"></td><td><input type="text" v-model="name[1]"></td><td><input type="text" v-model="url[1]"></td><td class="link" @click="deleteConfig(2)">删除</td>      	      
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
        code:[],
	name:[],
	url:[],
	configs:[],
      }
    },
    methods:{
      editConfig(){
        this.toggleShow();
        this.code = [1,2];
	this.name = ['隐私政策','用户协议'];
	this.url = ['mengqu.leanapp.cn/privacy','mengqu.leanapp.cn/protocol'];
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
	  this.configs = allConfigs;
	  let filterConfigs = this.configs.filter(
	    function(configs){
	      return configs.length != 0;
	    }
	  );
	  let finalFilterConfigs = filterConfigs.map(
	    function(config){
              var obj = {};
	      obj['code'] = config[0];
	      obj['name'] = config[1];
	      obj['url'] = config[2];
	      return obj;
	    }
	  );
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
	    
	      axios.post('/xxx/xxx', {
		    content:finalFilterConfigs 
		  })
		  .then(function (response) {
		    swal("你传送了"+finalFilterConfigs);
		  })
		  .catch(function (error) {
		    swal("你传送了"+finalFilterConfigs+"但是目前api是/xx/xx")
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


