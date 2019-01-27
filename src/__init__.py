AIRPORT_SETTINGS = {
  'LPPR': _LPPR,
  'LPCS': _LPCS,
  'LPPT': _LPPT,
  'LPFR': _LPFR,
  'LPMA': _LPMA,
}
=======
Euroscope Sweatbox Scenario Maker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Euroscope Sweatbox Scenario Maker. If not, see <http://www.gnu.org/licenses/>.
"""
import json

with open('data/airports.json', 'r') as file:
    AIRPORT_SETTINGS = json.loads(file.read())