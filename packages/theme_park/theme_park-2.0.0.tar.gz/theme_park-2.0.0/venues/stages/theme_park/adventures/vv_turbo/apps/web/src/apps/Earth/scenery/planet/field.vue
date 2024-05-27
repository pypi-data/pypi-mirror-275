


<script>
	import { field } from './field.js'
	export default field
</script>

<style>



</style>

<template>
	<div
		:style="{
			width: '100vw',
			height: '100vh',			
			
			boxSizing: 'border-box',
			padding: '.5in',
			background: 'black',
			color: 'white'
		}"
	>
		<nav
			:style="{
				display: 'flex',
				justifyContent: 'space-between',
				
				width: '100vw',
				height: '90px',			
				
				boxSizing: 'border-box',
				background: 'black',
				color: 'white'
			}"
		>
			<div>
				theme park
			</div>
			
			<div>
				<button>options</button>
				<button>shares</button>
				<button>businesses</button>
				
				<button>Trading View Riders</button>
			</div>
			
			<div></div>
			
		</nav>
	</div>
</template>

