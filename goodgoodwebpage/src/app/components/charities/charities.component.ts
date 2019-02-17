import {Component, Input, OnInit} from '@angular/core';
import {SearchService} from "../../services/search.service";


@Component({
  selector: 'app-charities',
  templateUrl: './charities.component.html',
  styleUrls: ['./charities.component.scss']
})
export class CharitiesComponent implements OnInit {
  @Input() values;
  skuString:String;

  constructor(private searchService: SearchService) {
      /*for(let index in this.values){
        if(this.values[0] == index){
          this.skuString = index.sku;
        }
        this.skuString += ","+index.sku;
      }
      this.searchService.charitySearch(this.skuString).subscribe((data)=>{

      });*/
  }

  ngOnInit() {
  }

}
