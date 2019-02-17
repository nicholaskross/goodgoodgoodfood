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
}
