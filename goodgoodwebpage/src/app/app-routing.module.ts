import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {CharitiesComponent} from "./components/charities/charities.component";
import {HomeComponent} from "./components/home/home.component";

const routes: Routes = [{
  path: "charities",
  component: CharitiesComponent
},{
  path: '',
  component: HomeComponent
},
  {
    path: "",
    redirectTo: '',
    pathMatch: 'full'
  }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
