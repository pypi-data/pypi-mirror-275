#
#  BEGIN LICENSE
#  Copyright (c) Blue Mind SAS, 2012-2016
#
#  This file is part of BlueMind. BlueMind is a messaging and collaborative
#  solution.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of either the GNU Affero General Public License as
#  published by the Free Software Foundation (version 3 of the License).
#
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#  See LICENSE.txt
#  END LICENSE
#
import requests
from netbluemind.python import serder

from netbluemind.core.container.api.ContainerSubscriptionModel import ContainerSubscriptionModel
from netbluemind.core.container.api.ContainerSubscriptionModel import __ContainerSubscriptionModelSerDer__


class ContainerSubscriptionDescriptor (ContainerSubscriptionModel):
    def __init__(self):
        ContainerSubscriptionModel.__init__(self)
        self.ownerDisplayName = None
        self.ownerDirEntryPath = None
        pass


class __ContainerSubscriptionDescriptorSerDer__:
    def __init__(self):
        pass

    def parse(self, value):
        if (value == None):
            return None
        instance = ContainerSubscriptionDescriptor()

        self.parseInternal(value, instance)
        return instance

    def parseInternal(self, value, instance):
        __ContainerSubscriptionModelSerDer__().parseInternal(value, instance)
        ownerDisplayNameValue = value['ownerDisplayName']
        instance.ownerDisplayName = serder.STRING.parse(ownerDisplayNameValue)
        ownerDirEntryPathValue = value['ownerDirEntryPath']
        instance.ownerDirEntryPath = serder.STRING.parse(
            ownerDirEntryPathValue)
        return instance

    def encode(self, value):
        if (value == None):
            return None
        instance = dict()
        self.encodeInternal(value, instance)
        return instance

    def encodeInternal(self, value, instance):
        __ContainerSubscriptionModelSerDer__().encodeInternal(value, instance)

        ownerDisplayNameValue = value.ownerDisplayName
        instance["ownerDisplayName"] = serder.STRING.encode(
            ownerDisplayNameValue)
        ownerDirEntryPathValue = value.ownerDirEntryPath
        instance["ownerDirEntryPath"] = serder.STRING.encode(
            ownerDirEntryPathValue)
        return instance
