import {RecipeModel} from '~/types/model-types';

export interface ResponseType<Data> {
    data: Data,
    status: string
}