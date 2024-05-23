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


class Promote:
    def __init__(self):
        self.mailboxUid = None
        self.folder = None
        self.hsmId = None
        self.imapUid = None
        self.internalDate = None
        self.flags = None
        pass


class __PromoteSerDer__:
    def __init__(self):
        pass

    def parse(self, value):
        if (value == None):
            return None
        instance = Promote()

        self.parseInternal(value, instance)
        return instance

    def parseInternal(self, value, instance):
        mailboxUidValue = value['mailboxUid']
        instance.mailboxUid = serder.STRING.parse(mailboxUidValue)
        folderValue = value['folder']
        instance.folder = serder.STRING.parse(folderValue)
        hsmIdValue = value['hsmId']
        instance.hsmId = serder.STRING.parse(hsmIdValue)
        imapUidValue = value['imapUid']
        instance.imapUid = serder.INT.parse(imapUidValue)
        internalDateValue = value['internalDate']
        instance.internalDate = serder.DATE.parse(internalDateValue)
        flagsValue = value['flags']
        instance.flags = serder.SetSerDer(serder.STRING).parse(flagsValue)
        return instance

    def encode(self, value):
        if (value == None):
            return None
        instance = dict()
        self.encodeInternal(value, instance)
        return instance

    def encodeInternal(self, value, instance):

        mailboxUidValue = value.mailboxUid
        instance["mailboxUid"] = serder.STRING.encode(mailboxUidValue)
        folderValue = value.folder
        instance["folder"] = serder.STRING.encode(folderValue)
        hsmIdValue = value.hsmId
        instance["hsmId"] = serder.STRING.encode(hsmIdValue)
        imapUidValue = value.imapUid
        instance["imapUid"] = serder.INT.encode(imapUidValue)
        internalDateValue = value.internalDate
        instance["internalDate"] = serder.DATE.encode(internalDateValue)
        flagsValue = value.flags
        instance["flags"] = serder.SetSerDer(serder.STRING).encode(flagsValue)
        return instance
