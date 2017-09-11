<template>
    <div class="searchStockCategoryVue">
		<form class="form-inline">
		  <div class="form-group" @click="clickFirst()">
		    <label for="first">一级分类</label>
		    <select class="form-control" id="first" v-model="firstCate"  @change="changeSecond()">
			    <option disabled value="">请选择一级分类</option>
				<option disabled value="">--------</option>
				<option disabled value="">--------</option>
		    </select>
		  </div>
		  <div class="form-group">
			    <label for="second">二级分类</label>
			    <select class="form-control" id="second" v-model="secondCate">
			        <option disabled value="">必须先选择一级分类</option>
					<option value="">"不选"</option>
			    </select>
		  </div>
		  <button type="submit" class="btn btn-default">搜索</button>
		</form> 
    </div>
</template>

<script>
  export default{

    data:function(){
      return {
        first:[],
		second:[],
		firstCate:"",
		secondCate:"",
      }
    },   
    props:['marketcategorys'],
    methods:{      
        clickFirst(){	
		  let firstName = [];
		  let _this = this;
		  let addedFirst = "";
		  let addedStuff = $('.addedFirst');
	      if(addedStuff.hasClass('addedFirst')){

		  }else{
			  if(this.marketcategorys != null){
				  this.marketcategorys.forEach(
				    function(item,index){
				      firstName[index] = item.name;
				      let secondName = [];
				      let secondCategory = item.saleCategorySecond;
				      if(secondCategory != null){
					      secondCategory.forEach(
					        function(item,index){
						  	secondName[index] = item;
						  });
				     	 _this.second[index] = secondName;	
				      }      
				      addedFirst += "<option class='addedFirst' value='"+index+"'>"+item.name+"</option>"	
				  });
				  this.first = firstName;
			  }else{
			  	this.first = [];
			  }
			  $(addedFirst).appendTo('select#first');
		  } 
		},
		changeSecond(){
		  let addedStuff = $('.addedSecond');
		  if(addedStuff.hasClass('addedSecond')){
		    $( ".addedSecond" ).remove();
		  }
	      let secondCate = this.firstCate;
		  let secondCates = this.second[secondCate];
		  let addedSecond = "";
		  secondCates.forEach(
		    function(item,index){
		      addedSecond += "<option class='addedSecond' value='"+index+"'>"+item.name+"</option>";
		  });
		  $(addedSecond).appendTo('select#second');
		  if(this.secondCate != ""){
		    this.changeThird();
		  }	        
       },
    },

}
</script>

<style>
select#first {
  padding: 0 50px;
}
</style>
