export class TemplateType1{
    id?:number;
    name:string;
    description:string;
    subMenu:string;
    templateType:string;
    pictures:ImageFile[];
    unitPrice:number;
    letterSpace?:boolean;
    colors?:Color[];
    bgColors?:Color[];

    options:{
        id?:number;
        active:boolean;
        title:string;
        subOptions:{
            id?:number;
            description:string;
            name:string;
            price:number;
        }[];
    }[];
}