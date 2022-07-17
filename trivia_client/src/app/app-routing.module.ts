import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { AuthGuard } from './_helpers/auth.guard';
import {TriviaComponent} from "@app/trivia/trivia.component";

const accountModule = () => import('./account/account.module').then(x => x.AccountModule);
const routes: Routes = [
  { path: '', component: HomeComponent, canActivate: [AuthGuard], title: 'Trivia Home' },
  { path: 'account', loadChildren: accountModule, title: 'Account' },
  { path: 'questions', component: TriviaComponent, canActivate: [AuthGuard], title: 'Questions'},

  // otherwise redirect to home
  { path: '**', redirectTo: '' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
