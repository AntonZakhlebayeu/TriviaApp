import { Component } from '@angular/core';

import { User } from '../_models/user';
import { Statistics } from '../_models/statistics'
import { AccountService } from '../_services/account.service';
import { StatisticsService} from "@app/_services/statistics.service";

@Component({ templateUrl: 'home.component.html' })
export class HomeComponent {
  user: User;
  statistics: Statistics;

  constructor(private accountService: AccountService, private statisticsService: StatisticsService) {
    this.user = this.accountService.userValue;
    this.statistics = this.statisticsService.getStatistics()
  }
}
