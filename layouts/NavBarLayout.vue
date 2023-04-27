<template>
    <div class="bg-primary h-16 grid grid-cols-3 place-items-center border-b-4 border-b-secondary rounded-b-2xl">
        <h1 class="text-4xl font-serif  font-black px-8">Recipe</h1>
        <slot name="center" class="col-start-2"/>
        <div class="col-start-2 empty:hidden">
            <slot name="center"/>
        </div>
        <div class="col-start-3 empty:hidden">
            <slot name="right"/>
        </div>
    </div>
    <slot/>
</template>