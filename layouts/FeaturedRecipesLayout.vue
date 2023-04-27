<template>
    <fieldset class="border border-secondary border-4 px-4 mx-4 rounded-2xl">
        <legend class="px-4"><h1 class="text-4xl font-bold text-center">Featured Recipes</h1></legend>
        <div class="grid place-items-center py-2">
            <slot name="search"/>
        </div>
        <div class="grid lg:grid-cols-2 3xl:grid-cols-3 gap-8 py-4">
            <slot name="featured"/>
        </div>
        <slot/>
    </fieldset>
</template>
<script setup>
</script>