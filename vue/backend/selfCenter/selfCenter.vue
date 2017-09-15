<template>
	<div class="selfcenterVue">
		<h2>个人信息</h2>
		<hr>
		<h3>账号:{{selfcenter.name}}</h3>
		<h3>角色:{{selfcenter.role}}</h3>
	</div>
</template>
<script type="text/javascript">
	export default {
		data:function(){
			return {

			}
		},
		props:["selfcenter"],
	}
</script>