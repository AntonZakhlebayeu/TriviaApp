import { Component } from '@angular/core';

import { AccountService } from './_services/account.service';
import { StatisticsService} from "@app/_services/statistics.service";
import { User } from './_models/user';
import { Statistics} from "@app/_models/statistics";

@Component({ selector: 'app', templateUrl: 'app.component.html' })
export class AppComponent {
  user: User;
  statistics: Statistics;
  title: any;

  constructor(private accountService: AccountService, private statisticsService: StatisticsService) {
    this.accountService.user.subscribe(x => this.user = x);
    this.statisticsService.statistics.subscribe(x => this.statistics = x);
  }

  logout() {
    this.accountService.logout();
    this.statisticsService.logout();
  }
}
