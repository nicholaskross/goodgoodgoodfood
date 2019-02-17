import { Component, OnInit } from '@angular/core';
import {FormGroup, FormControl} from "@angular/forms";
import {debounceTime, distinctUntilChanged} from "rxjs/operators";


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



  constructor() { }

  ngOnInit() {

    this.searchString.valueChanges
      .pipe(
        debounceTime(400),
        distinctUntilChanged()
      ).subscribe((value:string) => {
        console.log(value)
    })
  }

  get searchString(){
    return this.form.get('searchString')
  }



}
