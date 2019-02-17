import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {
  MatCardModule,
  MatDividerModule,
  MatExpansionModule, MatFormFieldModule,
  MatGridListModule, MatInputModule,
  MatToolbarModule,
  MatListModule, MatButtonModule
} from "@angular/material";
import { NavbarComponent } from './components/navbar/navbar.component';
import { SearchFilterComponent } from './components/search-filter/search-filter.component';
import {BrowserAnimationsModule} from "@angular/platform-browser/animations";
import {CartComponent} from "./components/cart/cart.component";
import {ItemComponent} from "./components/cart/item/item.component";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    SearchFilterComponent,
    NavbarComponent,
    CartComponent,
    ItemComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatToolbarModule,
    MatExpansionModule,
    BrowserAnimationsModule,
    MatCardModule,
    MatDividerModule,
    MatGridListModule,
    MatFormFieldModule,
    MatInputModule,
    FormsModule,
    ReactiveFormsModule,
    MatListModule,
    HttpClientModule,
    MatButtonModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
