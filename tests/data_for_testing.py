import requests


def refresh_xml():
    """
    A simple function to refresh the offline data set.


    :return:
    """
    xml = requests.get("http://syndication.enterprise.websiteidx.com/feeds/BoojCodeTest.xml").text.encode('utf-8')
    with open("feed_data.xml", 'w') as xml_file:
        xml_file.write(xml)
    xml_file.close()


# refresh_xml()

XML = """
<Listings>


  <Listing>


    <Location>

      <StreetAddress>0 Castro Peak Mountainway</StreetAddress>

      <UnitNumber/>

      <City>Malibu</City>

      <State>CA</State>

      <Zip>90265</Zip>

      <ParcelID/>

      <Lat>34.087528</Lat>

      <Long>-118.804301</Long>

      <County/>

      <StreetIntersection/>

      <DisplayAddress>Yes</DisplayAddress>

    </Location>

    <ListingDetails>

      <Status>Active</Status>

      <Price>535000.00</Price>

      <ListingUrl>http://www.thepartnerstrust.com/property/42921875/syn/43/</ListingUrl>

      <MlsId>14799273</MlsId>

      <MlsName>CLAW</MlsName>

      <ProviderListingId>42921875</ProviderListingId>

      <DateListed>2014-10-03 00:00:00</DateListed>

      <VirtualTourUrl><![CDATA[http://www.thepartnerstrust.com/property/42921875/syn/43/]]></VirtualTourUrl>

      <ListingEmail>zillow-41@leadrelay.com</ListingEmail>

      <AlwaysEmailAgent>0</AlwaysEmailAgent>

      <ShortSale/>

      <REO/>

    </ListingDetails>

    <RentalDetails>

      <Availability/>

      <LeaseTerm/>

      <DepositFees/>

      <UtilitiesIncluded>

	<Water/>

	<Sewage/>

	<Garbage/>

	<Electricity/>

	<Gas/>

	<Internet/>

	<Cable/>

	<SatTV/>

      </UtilitiesIncluded>

      <PetsAllowed>

	<NoPets/>

	<Cats/>

	<SmallDogs/>

	<LargeDogs/>

      </PetsAllowed>

    </RentalDetails>

    <BasicDetails>

      <PropertyType>VacantLand</PropertyType>

      <Title>0 Castro Peak Mountainway</Title>

      <Description><![CDATA[Enjoy amazing ocean and island views from this 10+ acre parcel situated in a convenient and peaceful area of the Santa Monica mountains. Just minutes from beaches or the 101, Castro Peak is located off of Latigo canyon in an area sprinkled with vineyards, ranches and horse properties. A paved road leads you to the site which features considerable useable land and multiple development areas. This is an area of new development. Build your dream.]]></Description>

      <Bedrooms>0</Bedrooms>

      <Bathrooms/>

      <FullBathrooms/>

      <HalfBathrooms/>

      <ThreeQuarterBathrooms/>

      <LivingArea/>

      <LotSize>10.82</LotSize>

      <year-built/>

    </BasicDetails>

    <Pictures>

              
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/0/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/1/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/2/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/3/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/4/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/5/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/6/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/7/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/8/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/9/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/10/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/11/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/12/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/13/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/14/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/15/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/16/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/17/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/18/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/19/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/20/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/21/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/22/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/23/v32/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42921875/24/v32/</PictureUrl>  	
<Caption/>	
</Picture>

    </Pictures>

    <Agent>

      <FirstName>Madison</FirstName>

      <LastName>Hildebrand</LastName>

      <EmailAddress>madison@themalibulife.com</EmailAddress>

      <PictureUrl>http://media.thepartnerstrust.com/pics/realtor/659891/107176/</PictureUrl>

      <OfficeLineNumber>310-818-5788</OfficeLineNumber>

      <MobilePhoneLineNumber>310-818-5788</MobilePhoneLineNumber>

      <FaxLineNumber/>

    </Agent>

    <Office>

      <BrokerageName>Partners Trust</BrokerageName>

      <BrokerPhone>310-858-6800</BrokerPhone>

      <BrokerEmail>inquire@thepartnerstrust.com</BrokerEmail>

      <BrokerWebsite>http://www.thepartnerstrust.com/</BrokerWebsite>

      <StreetAddress>23410 Civic Center Way, C1</StreetAddress>

      <UnitNumber/>

      <City>Malibu</City>

      <State>CA</State>

      <Zip>90265</Zip>

      <OfficeName>Malibu</OfficeName>

      <FranchiseName>Partners Trust</FranchiseName>

    </Office>

    <OpenHouses>

      <OpenHouse/>

    </OpenHouses>

    <Fees>

      <Fee>

	<FeeType/>

	<FeeAmount/>

	<FeePeriod>Monthly</FeePeriod>

      </Fee>

    </Fees>

    <Neighborhood>

      <Name/>

      <Description/>

    </Neighborhood>

    <RichDetails>

      <AdditionalFeatures/>

      <Appliances/>

      <ArchitectureStyle/>

      <Attic/>

      <BarbecueArea/>

      <Basement/>

      <BuildingUnitCount/>

      <CableReady/>

      <CeilingFan/>

      <CondoFloorNum/>

      <CoolingSystems>

	<CoolingSystem/>

      </CoolingSystems>

      <Deck/>

      <DisabledAccess/>

      <Dock/>

      <Doorman/>

      <DoublePaneWindows/>

      <Elevator>No</Elevator>

      <ExteriorTypes>

	<ExteriorType/>

      </ExteriorTypes>

      <Fireplace/>

      <FloorCoverings>

	<FloorCovering/>

      </FloorCoverings>

      <Garden/>

      <Gated/>

      <Greenhouse/>

      <HeatingFuels>

	<HeatingFuel/>

      </HeatingFuels>

      <HottubSpa/>

      <Intercom/>

      <JettedBathTub>No</JettedBathTub>

      <Lawn/>

      <LegalDescription/>

      <MotherInLaw/>

      <NumFloors/>

      <NumParkingSpaces/>

      <ParkingTypes>

	<ParkingType/>

      </ParkingTypes>

      <Patio/>

      <Pond/>

      <Pool/>

      <Porch/>

      <RoofTypes>

	<RoofType/>

      </RoofTypes>

      <RoomCount>0</RoomCount>

      <RvParking/>

      <Sauna/>

      <SecuritySystem>No</SecuritySystem>

      <Skylight/>

      <SportsCourt/>

      <SprinkerSystem/>

      <VaultedCeiling/>

      <ViewTypes>

	<ViewType/>

      </ViewTypes>

      <Waterfront/>

      <Wetbar/>

      <WhatOwnerLoves/>

      <Wired/>

      <YearUpdated/>

      <FitnessCenter/>

      <BasketballCourt/>

      <TennisCourt/>

      <NearTransportation/>

      <ControlledAccess/>

      <Over55ActiveCommunity/>

      <AssistedLivingCommunity/>

      <Storage/>

      <FencedYard/>

      <PropertyName/>

      <Furnished/>

      <HighspeedInternet/>

      <OnsiteLaundry/>

      <CableSatTV/>

      <Taxes>

	<Tax>

	  <TaxYear/>

	  <TaxAmount/>

	</Tax>

      </Taxes>

      <NewConstruction/>

    </RichDetails>

  </Listing>


  <Listing>

    <Location>

      <StreetAddress>0 SADDLE PEAK RD</StreetAddress>

      <UnitNumber/>

      <City>Malibu</City>

      <State>CA</State>

      <Zip>90290</Zip>

      <ParcelID/>

      <Lat>34.077269</Lat>

      <Long>-118.614425</Long>

      <County/>

      <StreetIntersection/>

      <DisplayAddress>Yes</DisplayAddress>

    </Location>

    <ListingDetails>

      <Status>Active</Status>

      <Price>200000.00</Price>

      <ListingUrl>http://www.thepartnerstrust.com/property/42922064/syn/43/</ListingUrl>

      <MlsId>14802845</MlsId>

      <MlsName>CLAW</MlsName>

      <ProviderListingId>42922064</ProviderListingId>

      <DateListed>2014-10-17 00:00:00</DateListed>

      <VirtualTourUrl><![CDATA[http://www.thepartnerstrust.com/property/42922064/syn/43/]]></VirtualTourUrl>

      <ListingEmail>zillow-41@leadrelay.com</ListingEmail>

      <AlwaysEmailAgent>0</AlwaysEmailAgent>

      <ShortSale/>

      <REO/>

    </ListingDetails>

    <RentalDetails>

      <Availability/>

      <LeaseTerm/>

      <DepositFees/>

      <UtilitiesIncluded>

	<Water/>

	<Sewage/>

	<Garbage/>

	<Electricity/>

	<Gas/>

	<Internet/>

	<Cable/>

	<SatTV/>

      </UtilitiesIncluded>

      <PetsAllowed>

	<NoPets/>

	<Cats/>

	<SmallDogs/>

	<LargeDogs/>

      </PetsAllowed>

    </RentalDetails>

    <BasicDetails>

      <PropertyType>VacantLand</PropertyType>

      <Title>0 SADDLE PEAK RD</Title>

      <Description><![CDATA[Spectacular views from this 4+ acre property perched on the ridge between PCH and the Valley. Two APNs - 4438-034-037 and 031 being sold together. Plus, there is a lot next door for sale too! A, paved private road leads you almost to the site. This lot has development challenges - not for the faint of heart. Property has been owned by the same family for over 40 years. Reports and information is limited.]]></Description>

      <Bedrooms>0</Bedrooms>

      <Bathrooms/>

      <FullBathrooms/>

      <HalfBathrooms/>

      <ThreeQuarterBathrooms/>

      <LivingArea/>

      <LotSize>4.2</LotSize>

      <year-built/>

    </BasicDetails>

    <Pictures>

              
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42922064/0/v7/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42922064/1/v7/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42922064/2/v7/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42922064/3/v7/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42922064/4/v7/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42922064/5/v7/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42922064/6/v7/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42922064/7/v7/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42922064/8/v7/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42922064/9/v7/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42922064/10/v7/</PictureUrl>  	
<Caption/>	
</Picture>
        
	<Picture>
<PictureUrl>http://media.thepartnerstrust.com/pics/property/42922064/11/v7/</PictureUrl>  	
<Caption/>	
</Picture>

    </Pictures>

    <Agent>

      <FirstName>Madison</FirstName>

      <LastName>Hildebrand</LastName>

      <EmailAddress>madison@themalibulife.com</EmailAddress>

      <PictureUrl>http://media.thepartnerstrust.com/pics/realtor/659891/107176/</PictureUrl>

      <OfficeLineNumber>310-818-5788</OfficeLineNumber>

      <MobilePhoneLineNumber>310-818-5788</MobilePhoneLineNumber>

      <FaxLineNumber/>

    </Agent>

    <Office>

      <BrokerageName>Partners Trust</BrokerageName>

      <BrokerPhone>310-858-6800</BrokerPhone>

      <BrokerEmail>inquire@thepartnerstrust.com</BrokerEmail>

      <BrokerWebsite>http://www.thepartnerstrust.com/</BrokerWebsite>

      <StreetAddress>23410 Civic Center Way, C1</StreetAddress>

      <UnitNumber/>

      <City>Malibu</City>

      <State>CA</State>

      <Zip>90265</Zip>

      <OfficeName>Malibu</OfficeName>

      <FranchiseName>Partners Trust</FranchiseName>

    </Office>

    <OpenHouses>

      <OpenHouse/>

    </OpenHouses>

    <Fees>

      <Fee>

	<FeeType/>

	<FeeAmount/>

	<FeePeriod>Monthly</FeePeriod>

      </Fee>

    </Fees>

    <Neighborhood>

      <Name/>

      <Description/>

    </Neighborhood>

    <RichDetails>

      <AdditionalFeatures/>

      <Appliances/>

      <ArchitectureStyle/>

      <Attic/>

      <BarbecueArea/>

      <Basement/>

      <BuildingUnitCount/>

      <CableReady/>

      <CeilingFan/>

      <CondoFloorNum/>

      <CoolingSystems>

	<CoolingSystem/>

      </CoolingSystems>

      <Deck/>

      <DisabledAccess/>

      <Dock/>

      <Doorman/>

      <DoublePaneWindows/>

      <Elevator>No</Elevator>

      <ExteriorTypes>

	<ExteriorType/>

      </ExteriorTypes>

      <Fireplace/>

      <FloorCoverings>

	<FloorCovering/>

      </FloorCoverings>

      <Garden/>

      <Gated/>

      <Greenhouse/>

      <HeatingFuels>

	<HeatingFuel/>

      </HeatingFuels>

      <HottubSpa/>

      <Intercom/>

      <JettedBathTub>No</JettedBathTub>

      <Lawn/>

      <LegalDescription/>

      <MotherInLaw/>

      <NumFloors/>

      <NumParkingSpaces/>

      <ParkingTypes>

	<ParkingType/>

      </ParkingTypes>

      <Patio/>

      <Pond/>

      <Pool/>

      <Porch/>

      <RoofTypes>

	<RoofType/>

      </RoofTypes>

      <RoomCount>0</RoomCount>

      <RvParking/>

      <Sauna/>

      <SecuritySystem>No</SecuritySystem>

      <Skylight/>

      <SportsCourt/>

      <SprinkerSystem/>

      <VaultedCeiling/>

      <ViewTypes>

	<ViewType/>

      </ViewTypes>

      <Waterfront/>

      <Wetbar/>

      <WhatOwnerLoves/>

      <Wired/>

      <YearUpdated/>

      <FitnessCenter/>

      <BasketballCourt/>

      <TennisCourt/>

      <NearTransportation/>

      <ControlledAccess/>

      <Over55ActiveCommunity/>

      <AssistedLivingCommunity/>

      <Storage/>

      <FencedYard/>

      <PropertyName/>

      <Furnished/>

      <HighspeedInternet/>

      <OnsiteLaundry/>

      <CableSatTV/>

      <Taxes>

	<Tax>

	  <TaxYear/>

	  <TaxAmount/>

	</Tax>

      </Taxes>

      <NewConstruction/>

    </RichDetails>

  </Listing>

</Listings>
"""
