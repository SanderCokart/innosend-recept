<template>
    <NuxtLayout name="featured-recipes-layout" class="mt-4">
        <template #search>
            <div class="grid grid-cols-[1fr,auto] max-w-screen-md w-full relative">
                <input v-model="search" type="text" class="rounded w-full text-black"
                       placeholder="Search..."/>
                <VChip class="absolute top-1/2 -translate-y-1/2 right-1" v-if="search !== debouncedSearch">
                    Searching...
                </VChip>
            </div>
        </template>
        <template #featured>
            <div class="md:col-span-3" v-if="!filteredFeaturedRecipes?.length">
                <h1 class="text-center font-medium">No recipes found</h1>
            </div>
            <article v-for="recipe in filteredFeaturedRecipes">
                <TheFeaturedRecipeCard :recipe="recipe"/>
            </article>
        </template>
    </NuxtLayout>
</template>

<script lang="ts" setup>

import {RecipeModel} from '~/types/model-types';
import {useDebounce} from '@vueuse/core';

const { data: recipes } = useFetch<{ data: RecipeModel[], status: string }, {}>('/recipes', {
    baseURL: useRuntimeConfig().public.API_URL
});

const search = ref('');
const filteredFeaturedRecipes = computed(() =>
    recipes.value?.data.filter(recipe => (
        recipe.featured
        && (
            recipe.title.toLowerCase().includes(debouncedSearch.value.toLowerCase())
            || recipe.category.toLowerCase().includes(debouncedSearch.value.toLowerCase())
        )))
);

const debouncedSearch = useDebounce(search, 500);


</script>