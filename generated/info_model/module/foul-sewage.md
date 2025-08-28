# Foul sewage disposal

Information about foul sewage disposal methods and connection to existing 
drainage systems for development proposals


| has-new-disposal-arrangements | Has new disposal arrangements | Does the proposal include any new foul sewage disposal arrangments |  | MUST |  |
| foul-sewage-disposal-types | Foul sewage disposal types[] | List of ways foul sewage will be disposed of |  | MAY | Select from the **foul-sewage-disposal-type** enum |
| produce-foul-sewage | Produce foul sewage | Whether the proposed development will produce any foul sewage |  | MUST |  |
| connect-to-drainage-system | Connect to drainage system | Whether the proposal needs to connect to the existing drainage system |  | MUST |  |
| drainage-system-details | Drainage system details | Details of the drawings/plans that show the existing drainage system |  | MAY |  |

**Validation rules**

- if connect-to-drainage-system == true then drainage-system-details is required
- if application-type includes 'extraction-oil-gas' then drainage-system-details is required