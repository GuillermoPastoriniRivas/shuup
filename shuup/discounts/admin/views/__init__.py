# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2021, Shuup Commerce Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from ._active_list import DiscountListView
from ._archive import ArchivedDiscountListView
from ._delete import DiscountDeleteView
from ._edit import DiscountEditView
from ._happy_hours import HappyHourDeleteView, HappyHourEditView, HappyHourListView

__all__ = [
    "ArchivedDiscountListView",
    "DiscountDeleteView",
    "DiscountEditView",
    "DiscountListView",
    "HappyHourEditView",
    "HappyHourDeleteView",
    "HappyHourListView",
]
