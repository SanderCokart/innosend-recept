<template>
    <div class="grid md:grid-cols-2 gap-x-4 gap-y-2 md:gap-y-1 grid-rows-[auto,1fr] h-full relative">
        <h1 class="text-2xl font-bold md:col-span-2">{{ recipe.title }}</h1>
        <figure class="w-full h-full relative md:static">
            <div class="relative h-full w-full">
                <img :src="recipe.image"
                     class="h-full w-full object-cover aspect-square border-secondary border-4 border-b-0 rounded-t-2xl"
                     alt="{{recipe.title}}"/>
                <Icon name="material-symbols:favorite-rounded" class="text-white text-xl absolute bottom-0"
                      :class="{
                                'text-secondary': recipe.favorite,
                            }"/>
            </div>
            <figcaption
                    class="absolute bottom-0 inset-x-0 bg-primary font-medium p-2">
                {{ recipe.short_description }}
            </figcaption>
        </figure>

        <div class="bg-bodyLight w-full flex flex-col gap-8 border-primary p-4 md:px-2 md:py-1 border-4">
            <p class="leading-relaxed font-medium text-lg">{{ recipe.long_description }}</p>
            <div class="flex flex-wrap gap-4 mb-10">
                <VChip>{{ recipe.category }}</VChip>
                <VChip class="inline-flex items-center gap-1">
                    <Icon name="fluent-emoji-high-contrast:fork-and-knife-with-plate"/>
                    {{ recipe.serving_size }}
                </VChip>
                <VChip class="inline-flex items-center gap-1">
                    <Icon name="streamline:interface-time-hour-glass-hourglass-loading-measure-clock-time"/>
                    {{ recipe.cooking_time }}
                </VChip>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import type {RecipeModel} from '~/types/model-types';

defineProps<{
    recipe: RecipeModel
}>();
</script>