import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {environment} from "../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  constructor(private http: HttpClient) {}


  itemSearch(searchString: string){
    console.log(searchString);
    return this.http.get(`${environment.baseURL}/search?query=${searchString}`);
  }

  charitySearch(skuString: string){
    //may need to spit and add , to this string??
    return this.http.get(`${environment.baseURL}/charity?skus=${skuString}`);
  }

  getGeneric(searchString: string){
    console.log(searchString);
    return this.http.get(`${environment.baseURL}/similar?sku=${searchString}`)
  }
}
