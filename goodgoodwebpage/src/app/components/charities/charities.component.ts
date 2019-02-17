import {Component, Input, OnInit} from '@angular/core';
import {SearchService} from "../../services/search.service";
import {ActivatedRoute} from "@angular/router";


@Component({
  selector: 'app-charities',
  templateUrl: './charities.component.html',
  styleUrls: ['./charities.component.scss']
})
export class CharitiesComponent implements OnInit {
  skuString: string;

  constructor(private searchService: SearchService,private route: ActivatedRoute) {

  }

  ngOnInit() {
      let values = this.route.snapshot.paramMap.get("values");
    for(let index in values){
      if(values[0] == index){
        //this.skuString = index.sku;
      }
      //this.skuString += ","+index.sku;
    }
    this.searchService.charitySearch(this.skuString).subscribe((data)=>{

    });
  }

}
