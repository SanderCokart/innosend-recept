# Innosend Recipe | Nuxt 3

This project was build with [Nuxt 3](https://v3.nuxtjs.org) and [Tailwind CSS](https://tailwindcss.com/).

## Getting Started

### Installation

```bash
pnpm install && pnpm dev
```

### Environment

Copy .env.example as .env

This project uses a dummy backend found in `./backend` folder. To start the backend, run

```bash
python backend.py
```

in a separate terminal instance.

**IMPORTANT**: You must run the command from the `./backend` folder.

## Included Features

- [x] Search for recipes based on title and category
- [ ] Filter recipes by category
- [ ] View recipe details
- [ ] Add recipe to favorites
- [ ] List of all recipes
- [ ] Recipes page

## Why Nuxt

The task assigned to me was to build a landing page and some other pages indicating it was a website and not a webapp.
I was restricted to Vue so there was only one logical solution: Nuxt.

Nuxt is like Next for React except it's for Vue.

## First Impressions

While Nuxt gets a lot of things right it has seemingly a lot of typescript issues as of making this assignment.
Especially when using composables such as `useFetch`.

## What I liked

Nuxt has more features right now compared to Next with the new layout structure and all. Also the ready to use modules
you can easily install are very cool.

Next is still in the process of getting similar features working properly with their new `app` directory structure.

Nuxt's way of doing layout is awesome and I love it. I have not tested yet if it can share state without the use
of `useState` but I am eager to find out.

## What I didn't like

Typescript pretty much is all I dislike about it.
The making of custom composables to make something as simple as a useFetch that includes the `baseURL:` is more
complicated than it has to be.
At least provided you want to give your custom composables the same level of type hinting as the original useFetch has.

If there are other ways of dealing with this I'd love to know. And feel free to do a **PR**.

There s also seemingly no way to use .env variables to enable things like debug in the `./nuxt.config.ts` file.
They are only allowed within the `runtimeConfig` object within the config file.

## Other things

### Naming convention

I tried to abide by a naming convention that is more common in the Vue community.
This means if a component is prefixed with `V` or `Base` it occurs more than once in the project.
If it is prefixed with `The` it only occurs once in the project.

Despite layouts being in the `./layouts` folder I still suffix them with `Layout` because this makes them easier to find
in IDE's.

I try to make sure that anything that is a major layout component is defined as a layout whereas the components within
that layout have a
layout of their own internally they require to be responsive on their own within their expected container size.

### Package manager

`pnpm` is just the fastest by a long shot.

### Feature elaboration

* Search is debounced by 500ms to prevent too many requests being sent to the backend.

### Tailwind config

I added custom colors to make styling later on easier once a client has figured out their colorscheme.

I added extra functionality by adding spacing to the minHeight.

I also added more breakpoints to support a wider range of devices. I know for a fact the IPhone SE is 320px wide on
browsers which is one of the smallest phones in use today.