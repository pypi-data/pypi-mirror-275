#  Copyright (c) 2024 Ubiterra Corporation. All rights reserved.
#  #
#  This ZoneVu Python SDK software is the property of Ubiterra Corporation.
#  You shall use it only in accordance with the terms of the ZoneVu Service Agreement.
#  #
#  This software is made available on PyPI for download and use. However, it is NOT open source.
#  Unauthorized copying, modification, or distribution of this software is strictly prohibited.
#  #
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#  INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
#  PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
#  FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#  ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#
#
#
#
#

from typing import Union, List, Optional
from .Client import Client
from .Error import ZonevuError
from strenum import StrEnum
from ..DataModels.Geospatial.Crs import CrsSpec, CrsEntry
from ..DataModels.Geospatial.Coordinate import Coordinate
from ..DataModels.Geospatial.GeoLocation import GeoLocation
from ..DataModels.Geospatial.GridGeometry import GridGeometry
from ..DataModels.Geospatial.Enums import DistanceUnitsEnum
from ..DataModels.Geomodels.SimpleGrid import SimpleGrid


class StateCode(StrEnum):
    AL = 'Alabama'
    AK = 'Alaska'
    AZ = 'Arizona'
    AR = 'Arkansas'
    CA = 'California'
    CO = 'Colorado'
    CT = 'Connecticut'
    DE = 'Delaware'
    FL = 'Florida'
    GA = 'Georgia'
    HI = 'Hawaii'
    ID = 'Idaho'
    IL = 'Illinois'
    IN = 'Indiana'
    IA = 'Iowa'
    KS = 'Kansas'
    KY = 'Kentucky'
    LA = 'Louisiana'
    ME = 'Maine'
    MD = 'Maryland'
    MA = 'Massachusetts'
    MI = 'Michigan'
    MN = 'Minnesota'
    MS = 'Mississippi'
    MO = 'Missouri'
    MT = 'Montana'
    NE = 'Nebraska'
    NV = 'Nevada'
    NH = 'New Hampshire'
    NJ = 'New Jersey'
    NM = 'New Mexico'
    NY = 'New York'
    NC = 'North Carolina'
    ND = 'North Dakota'
    OH = 'Ohio'
    OK = 'Oklahoma'
    OR = 'Oregon'
    PA = 'Pennsylvania'
    RI = 'Rhode Island'
    SC = 'South Carolina'
    SD = 'South Dakota'
    TN = 'Tennessee'
    TX = 'Texas'
    UT = 'Utah'
    VT = 'Vermont'
    VA = 'Virginia'
    WA = 'Washington'
    WV = 'West Virginia'
    WI = 'Wisconsin'
    WY = 'Wyoming'


class Datum(StrEnum):
    NAD27 = 'Nad1927'
    NAD83 = 'Nad1983'
    WGS1984 = 'Wgs1984'


class StateZone(StrEnum):
    North = 'North'
    South = 'South'
    East = 'East'
    West = 'West'
    Central = 'Central'
    SouthCentral = 'SouthCentral'
    EastCentral = 'EastCentral'
    WestCentral = 'WestCentral'
    I = 'I'
    II = 'II'
    III = 'III'
    IV = 'IV'
    V = 'V'
    VI = 'VI'
    VII = 'VII'


class UtmZone(StrEnum):
    N = 'N'
    S = 'S'


class CoordinatesService:
    client: Client

    def __init__(self, c: Client):
        self.client = c

    def convert_epsg(self, epsg: int) -> CrsSpec:
        try:
            item = self.client.get('coordinates/epsg/%s' % epsg, None, False)
            return CrsSpec.from_dict(item)
        except ZonevuError as err:
            raise ZonevuError.local('could not find coordinate reference system for EPSG code %s because %s' %
                                    (epsg, err.message))

    def get_geolocation(self, c: Coordinate, crs: CrsSpec) -> GeoLocation:
        item = self.client.get('coordinates/geolocation', {"x": c.x, "y": c.y, "epsgcode": crs.epsg_code,
                                                           "projection": crs.projection, "zone": crs.zone,
                                                           "units": '' if crs.units is None else crs.units}, False)
        return GeoLocation.from_dict(item)

    def get_geolocations(self, xys: List[Coordinate], crs: CrsSpec) -> List[GeoLocation]:
        xy_json_array = [c.to_dict() for c in xys]
        items = self.client.post_return_list('coordinates/geolocations', xy_json_array, False, {"epsgcode": crs.epsg_code,
                                "projection": crs.projection, "zone": crs.zone,
                                "units": '' if crs.units is None else crs.units})
        locations = [GeoLocation.from_dict(item) for item in items]
        return locations

    def get_coordinate(self, loc: GeoLocation, crs: CrsSpec) -> Coordinate:
        item = self.client.get('coordinates/coordinate', {"latitude": loc.latitude, "longitude": loc.longitude,
                                                          "epsgcode": crs.epsg_code,
                                                          "projection": crs.projection, "zone": crs.zone,
                                                          "units": '' if crs.units is None else crs.units}, False)
        return Coordinate.from_dict(item)

    def get_projections(self) -> list[CrsEntry]:
        items: list[str] = self.client.get_list('coordinates/projections', None, False)
        entries = [CrsEntry.from_dict(w) for w in items]
        return entries

    def get_zones(self, projection: str) -> list[CrsEntry]:
        items: list[str] = self.client.get_list('coordinates/zones', {"projection": projection}, False)
        entries = [CrsEntry.from_dict(w) for w in items]
        return entries

    def get_stateplane_crs(self, state: StateCode, datum: Datum, state_zone: Union[StateZone, int],
                           units: Optional[DistanceUnitsEnum] = DistanceUnitsEnum.Undefined) -> Optional[CrsSpec]:
        """
        Attempts to find the state plane CRS by name
        """
        state_str = str(state)
        state_plane_projection = str('StatePlane%s' % datum)
        zone_str = str(state_zone)
        zone_name_fragment = '%s %s' % (state_str, zone_str)

        projections = self.get_projections()
        projection = next((p for p in projections if p.id == state_plane_projection), None)
        if projection is None:
            return None
        zones = self.get_zones(projection.id)
        zone = next((z for z in zones if z.name.startswith(zone_name_fragment)), None)
        if zone is None:
            return None

        return CrsSpec(None, projection.id, zone.id, units)

    def get_utm_crs(self, datum: Datum, zone_number: int, zone_letter: UtmZone,
                    units: Optional[DistanceUnitsEnum] = DistanceUnitsEnum.Undefined) -> Optional[CrsSpec]:
        projection_str = str('Utm%s' % datum)
        zone_base = '%s%s' % (zone_number, zone_letter)
        zone_str = str('%sUtmZone%s' % (datum, zone_base)).lower()

        projections = self.get_projections()
        projection = next((p for p in projections if p.id == projection_str), None)
        if projection is None:
            return None

        zones = self.get_zones(projection.id)
        zone = next((z for z in zones if z.id.lower() == zone_str), None)
        if zone is None:
            return None

        return CrsSpec(None, projection.id, zone.id, units)

    def simple_to_grid_geometry(self, grid: SimpleGrid) -> GridGeometry:
        g = GridGeometry.from_simple_grid(grid)
        g.corner1.lat_long = self.get_geolocation(g.corner1.p, grid.crs)
        g.corner2.lat_long = self.get_geolocation(g.corner2.p, grid.crs)
        g.corner3.lat_long = self.get_geolocation(g.corner3.p, grid.crs)
        g.corner4.lat_long = self.get_geolocation(g.corner4.p, grid.crs)
        g.geo_inclination = GeoLocation.bearing(g.corner1.lat_long, g.corner4.lat_long)
        return g
