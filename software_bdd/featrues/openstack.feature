Feature: E2E OF OPENSTACk
#  Background: testing environment setting as qa
#    Given The evnironment is qa

  Scenario: Create a cinder
    Given sso_login cwe
    Then create cert type show
    When create osp "catagory_storage-3122943" "certification-filestorage-plugin" "Red Hat OpenStack Platform 11.0" "7.3"
    When feature-based manila "CIFS" "extend share"


