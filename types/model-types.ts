export interface RecipeModel {
    category: string;
    cooking_time: number;
    favorite: boolean;
    featured: boolean;
    id: number;
    image: string;
    ingredients: string[];
    instructions: string[];
    long_description: string;
    rating: number;
    serving_size: number;
    short_description: string;
    title: string;
}
