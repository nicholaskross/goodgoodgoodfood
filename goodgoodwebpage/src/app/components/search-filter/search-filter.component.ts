import { Component, OnInit } from '@angular/core';
import {FormGroup, FormControl} from "@angular/forms";
import {debounceTime, distinctUntilChanged} from "rxjs/operators";
import {SearchService} from "../../services/search.service";

@Component({
  selector: 'app-search-filter',
  templateUrl: './search-filter.component.html',
  styleUrls: ['./search-filter.component.scss']
})
export class SearchFilterComponent implements OnInit {
  private form: FormGroup = new FormGroup({
    searchString: new FormControl('', [
    ])
  });

  searchResults;


  constructor(private searchService: SearchService) { }

  ngOnInit() {

    this.searchString.valueChanges
      .pipe(
        debounceTime(400),
        distinctUntilChanged()
      ).subscribe((value:string) => {
      if (value !== '') {
        this.searchService.itemSearch(value).subscribe(
          data => {
            this.searchResults = data;
            console.log(this.searchResults)
          },
          error => {
            console.log(error)
          }
        )
      }
    });
  }

  get searchString(){
    return this.form.get('searchString')
  }



}
