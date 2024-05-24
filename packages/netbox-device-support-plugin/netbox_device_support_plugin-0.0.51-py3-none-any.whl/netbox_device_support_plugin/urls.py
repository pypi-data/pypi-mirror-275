from netbox.views.generic import ObjectChangeLogView
from django.urls import path
from . import views, models


app_name = "netbox_device_support_plugin"


urlpatterns = (
    # Cisco Device Support
    path(
        "cisco-device/",
        views.CiscoDeviceSupportListView.as_view(),
        name="ciscodevicesupport_list",
    ),
    path(
        "cisco-device/delete/",
        views.CiscoDeviceSupportBulkDeleteView.as_view(),
        name="ciscodevicesupport_bulk_delete",
    ),
    path(
        "cisco-device/<int:pk>/delete/",
        views.CiscoDeviceSupportDeleteView.as_view(),
        name="ciscodevicesupport_delete",
    ),
    path(
        "cisco-device/<int:pk>/changelog/",
        ObjectChangeLogView(
            base_template=f"{models.CiscoDeviceSupport._meta.app_label}/cisco/cisco_device_support_changelog.html").as_view(),
        name="ciscodevicesupport_changelog",
        kwargs={"model": models.CiscoDeviceSupport}
    ),
    # Cisco Device Type Support
    path(
        "cisco-device-type/",
        views.CiscoDeviceTypeSupportListView.as_view(),
        name="ciscodevicetypesupport_list",
    ),
    path(
        "cisco-device-type/delete/",
        views.CiscoDeviceTypeSupportBulkDeleteView.as_view(),
        name="ciscodevicetypesupport_bulk_delete",
    ),
    path(
        "cisco-device-type/<int:pk>/delete/",
        views.CiscoDeviceTypeSupportDeleteView.as_view(),
        name="ciscodevicetypesupport_delete",
    ),
    path(
        "cisco-device-type/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="ciscodevicetypesupport_changelog",
        kwargs={"model": models.CiscoDeviceTypeSupport}
    ),
    # Fortnet Support
    path(
        "fortinet-device/",
        views.FortinetDeviceSupportListView.as_view(),
        name="fortinetdevicesupport_list",
    ),
    path(
        "fortinet-device/delete/",
        views.FortinetDeviceSupportBulkDeleteView.as_view(),
        name="fortinetdevicesupport_bulk_delete",
    ),
    path(
        "fortinet-device/<int:pk>/delete/",
        views.FortinetDeviceSupportDeleteView.as_view(),
        name="fortinetdevicesupport_delete",
    ),
    path(
        "fortinet-device/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="fortinetdevicesupport_changelog",
        kwargs={"model": models.FortinetDeviceSupport}
    ),
    # PureStorage Support
    path(
        "purestorage-device/",
        views.PureStorageDeviceSupportListView.as_view(),
        name="purestoragedevicesupport_list",
    ),
    path(
        "purestorage-device/delete/",
        views.PureStorageDeviceSupportBulkDeleteView.as_view(),
        name="purestoragedevicesupport_bulk_delete",
    ),
    path(
        "purestorage-device/<int:pk>/delete/",
        views.PureStorageDeviceSupportDeleteView.as_view(),
        name="purestoragedevicesupport_delete",
    ),
    path(
        "purestorage-device/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="purestoragedevicesupport_changelog",
        kwargs={"model": models.PureStorageDeviceSupport}
    ),
)
